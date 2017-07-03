import requests as req
from bs4 import BeautifulSoup
import re
import csv
import json
from pprint import pprint






def parse():
	get_cookies = req.get("http://www.dochkisinochki.ru") #http://www.dochkisinochki.ru/shops/?show_all=Y
	cookies = get_cookies.cookies
	params = {
		"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
	}
	r = req.get("http://www.dochkisinochki.ru/shops/?show_all=Y", params=params, cookies=cookies);
	soup = BeautifulSoup(r.text, "lxml")
	page = soup.find(id="stores__container")
	print(page)
	shops = soup.find_all(class_="shop_element")
	for shop in shops:
		title = shop.find(class_="shop_element_title")[0].contents[0]
		print(title)

	
def parse_old():
	get_cookies = req.get("http://www.dochkisinochki.ru/shops/?show_all=Y") #http://www.dochkisinochki.ru/shops/?show_all=Y
	cookies = get_cookies.cookies
	params = {
		"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
	}
	r = req.get("http://www.dochkisinochki.ru/ajax/shops_getList.php", params=params, cookies=cookies);
	json = r.json(strict=False)
	stores = json['stores']
	for item in stores:
		row = []
		city_addr = item['name'].split(',')
		city = city_addr[0]
		address = ",".join(city_addr[1:])
		phone = item['phone']
		schedule = item['working_hours']
		comment = item['directions']
		
		row.append(city)
		row.append(address)
		row.append(comment)
		row.append(schedule)
		row.append(phone)
		row.append("Дочкисыночки")
	
		with open('./content/dochkisinochki.csv', 'a') as file:
			wr = csv.writer(file, dialect='excel', delimiter=';')
			wr.writerow(row)
			file.close()



with open('./content/dochkisinochki.csv', 'w') as file:
	file.close()

if __name__ == "__main__":
	parse()