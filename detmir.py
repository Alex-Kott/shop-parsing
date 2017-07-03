import requests as req
from bs4 import BeautifulSoup
import re
import csv
import time


def parse():
	r = req.get("https://www.detmir.ru/shops/?city=0")
	r.encoding = "utf-8"
	soup = BeautifulSoup(r.text, "lxml")
	result_search = soup.find("div", id="result_search")
	shops = result_search.find_all("tr")
	for tr in shops:
		format_ = tr.img['alt']
		contents = tr.find(class_="address-col").contents

		location = " ".join(str(x) for x in contents)
		location = re.sub(r'\s+', ' ', location)
		location = re.sub(r'<.*>', '', location)
		location = location.strip()

		city = re.findall(r'(.*г\.\s?\w+)', location)
		#city = re.findall(r'\.*[^,]*', location)
		if len(city) == 0:
			city = ''
			address = location
		else:
			city = city[0]
			address = location.replace(city, '')
			address = address.strip(', ')
		schedule = tr.find(class_="shop_time_work").contents[1]
		if city == '' and address == '':
			continue

		row = []
		row.append(city)
		row.append(address)
		row.append('')
		row.append(schedule)
		row.append('')
		row.append('Детский мир')
		row.append(format_)


		with open('./content/detmir.csv', 'a') as file:
			wr = csv.writer(file, dialect='excel', delimiter=';')
			wr.writerow(row)
			file.close()
	


def parse_old(): # парсил js-код. Это оказался неправильный путь, там в html всё нормально есть
	r = req.get("https://www.detmir.ru/shops/?city=0")
	r.encoding = "utf-8"
	page = r.text
	items = page.split("0188DD")
	del items[0]
	for i in items:
		soup = BeautifulSoup(i, "lxml")
		title = soup.a.contents[0]
		title = title.replace('Детский мир - ', '')
		addr_info = re.findall(r'<strong>Адрес:<\/strong>[^<>]*', i)
		address = addr_info[0]
		address = re.sub(r'<.*>', '', address)

		sched_info = re.findall(r'<strong>Время работы:<\/strong>[^<>]*', i)
		schedule = sched_info[0]
		schedule = re.sub(r'<.*>', '', schedule)
		
		city = address.split(',')[0]
		if city.find("г. ") == -1:
			city += address.split(',')[1]

		row = []
		row.append(city)
		row.append(address)
		row.append(title)
		row.append(schedule)
		
		with open('data.csv', 'a') as file:
			wr = csv.writer(file, dialect='excel', delimiter=';')
			wr.writerow(row)
			file.close()
		
	

with open('./content/detmir.csv', 'w') as file:
	file.close()

if __name__ == "__main__":
	parse()