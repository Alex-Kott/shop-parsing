import requests as req
from bs4 import BeautifulSoup
import re
import csv
import json
from pprint import pprint






def parse():
	r = req.get("https://raw.githubusercontent.com/Alex-Kott/shop-parsing/master/content/dochkisinochki.html");
	soup = BeautifulSoup(r.text, "lxml")
	shops = soup.find_all(class_="shop_element")
	for shop in shops:
		title = shop.find(class_="shop_element_title").a.contents[0]
		location = title.split(',')
		city = location[0]
		del location[0]
		address = ",".join(location)

		try:
			comment = shop.find(class_="dop_info").contents[0]
		except:
			comment = ''

		elem_property = shop.find_all(class_="shop_element_property")
		phone = elem_property[0].contents[0]
		schedule = elem_property[1].contents[0]

		row = []
		row.append(city)
		row.append(address)
		row.append(comment)
		row.append(schedule)
		row.append(phone)
		row.append("Дочкисыночки")
		row.append("")
		
		with open('./content/dochkisinochki.csv', 'a') as file:
			wr = csv.writer(file, dialect='excel', delimiter=';')
			wr.writerow(row)
			file.close()
		

	
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