import requests as req
from bs4 import BeautifulSoup
import re
import csv
import time



def parse():

	headers = {
		'Accept' 			: 'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding' 	: 'gzip, deflate, br',
		'Accept-Language' 	: 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4,bg;q=0.2',
		'Connection' 		: 'keep-alive',
		'Host'				: 'www.korablik.ru',
		'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
	}
	
	for i in range(1, 337):
		s = req.get("https://www.korablik.ru/shop/{}".format(i), headers=headers)
		s.encoding = "utf-8"
		page = s.text
		if page.find("Страница не найдена") != -1:
			continue
		soup = BeautifulSoup(s.text, "lxml")
		try:
			addr_info = soup.find_all(class_="shop_adress")[0]
		except:
			continue
		h1s = addr_info.find_all("h1")
		address = []
		for a in h1s:
			address.append(a.contents[0])

		address = ', '.join(address)
		addr = address.split(',')
		city = addr[0]
		if city.find("м. ") != -1:
			city = "Москва"
		else:
			del addr[0]
		address = ', '.join(addr)

		schedule = soup.find(class_="shop_time")
		schedule = re.sub(r'<.*>', '', str(schedule))
		schedule = re.sub(r'\s{2,}', ' ', schedule)

		shop_phone = soup.find_all(class_="shop_phone")[0]
		phone = shop_phone.find(class_="shop_info_content")

		phone = re.sub(r'<br\/>', ', ', str(phone))
		phone = re.sub(r'<.*>', '', phone)
		phone = re.sub(r'Телефон', ' ', phone)
		phone = re.sub(r'\s{2,}', ' ', phone)

		way = soup.find_all(class_="shop_way_text")
		try:
			comment = way[0].contents[0]
		except:
			comment = ''

		row = []
		row.append(city)
		row.append(address)
		row.append(comment)
		row.append(schedule)
		row.append(phone)
		row.append("Кораблик")

		with open('./content/korablik.csv', 'a') as file:
			wr = csv.writer(file, dialect='excel', delimiter=';')
			wr.writerow(row)
			file.close()


		
	'''with open('data.csv', 'a') as file:
								wr = csv.writer(file, dialect='excel', delimiter=';')
								wr.writerow(row)
								file.close()'''
		

with open('./content/korablik.csv', 'w') as file:
	file.close()

if __name__ == "__main__":
	parse()