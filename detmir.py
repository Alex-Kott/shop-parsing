import requests as req
from bs4 import BeautifulSoup
import re
import csv
import time



def parse():
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
		
		

if __name__ == "__main__":
	parse()