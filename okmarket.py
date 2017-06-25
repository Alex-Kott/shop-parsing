import requests as req
from bs4 import BeautifulSoup
import csv
import re

cities = {}

def parse():
	r = req.get("http://www.okmarket.ru/stores/")
	soup = BeautifulSoup(r.text, "lxml")
	options = soup.find_all("option")
	for opt in options:
		city_name = opt.contents[0]
		city_id = opt['value']
		cities[city_id] = city_name
	for city_id in cities:
		params = {	'arrFilterCat[PROPERTY_CITY]' : city_id,
					'IS_AJAX_FILTER' : 'Y',
					'SAVE_FILTER' : 'Y'}
		r = req.get('http://www.okmarket.ru/stores/', params=params)
		page = re.sub(r'\s', ' ', r.text) # все пробельные символы заменяем на пробелы
		page = re.sub(r'\s{2,}', ' ', r.text) # а потом последовательность из более, чем одного пробела заменяем на 1 пробел
		soup = BeautifulSoup(page, "lxml")
		items = soup.find_all(class_="shop-list-item")
		with open('data.csv', 'a') as file:
			wr = csv.writer(file, dialect='excel', delimiter=';')
			for item in items:
				row = []
				row.append(cities[city_id])
				item_address = item.find_all(class_="shop-list-item__adress")
				address = item_address[0].contents[0]
				row.append(address)

				item_comment = item.find_all(class_="shop-list-item__title-text")
				comment = item_comment[0].contents[0]
				comment += " (О'КЕЙ)"
				row.append(comment)

				item_schedule = item.find_all(class_="shop-list-item__time")
				schedule = item_schedule[0].contents[0]
				row.append(schedule)

				item_phone = item.find_all(class_="shop-list-item__phone-link")
				phone = item_phone[0].contents[0]
				row.append(phone)

				wr.writerow(row)

	file.close()
		




if __name__ == "__main__":
	parse()