import requests as req
from bs4 import BeautifulSoup
import re
import csv
import time

def giper(link, city):
	g = req.get(link+'/gipermarkety/')
	g.encoding = "utf-8"
	e404 = re.findall(r'\b404\b', g.text)
	if len(e404) > 0:
		return False
	#dot-market-type-1-style-2
	soup = BeautifulSoup(g.text, "lxml")
	gipers = soup.find_all(class_="dot-market-type-1-style-2")
	for gip in gipers:
		try:
			address = gip.a.contents[0]
		except:
			continue
		href = gip.a['href']
		d = req.get("http://www.lenta.com{}".format(href))
		d.encoding = "utf-8"
		text = re.sub(r'\&ndash;', '', d.text)
		sched_info = re.findall(r'Режим работы[^;]*;', text)
		schedule = ''
		if len(sched_info) > 0:
			schedule = sched_info[0]
			schedule = re.sub(r'<.*>', '', schedule)
		shop = BeautifulSoup(d.text, "lxml")
		blue2 = shop.find_all(class_="blue2")
		if len(blue2) > 0:
			blue2 = blue2[0]
			comment = blue2.strong.contents[0]
		else:
			blue2 = ''
			comment = ''
		

		row = []
		row.append(city)
		row.append(address)
		row.append(comment)
		row.append(schedule)
		row.append('')
		row.append('Лента')


		with open('data.csv', 'a') as file:
			wr = csv.writer(file, dialect='excel', delimiter=';')
			wr.writerow(row)
			file.close()


def super(link, city):
	s = req.get(link+'/supermarkety/')
	s.encoding = "utf-8"
	e404 = re.findall(r'\b404\b', s.text)
	if len(e404) > 0:
		return False
	#dot-market-type-2-style-2
	soup = BeautifulSoup(s.text, "lxml")
	supers = soup.find_all(class_="dot-market-type-2-style-2")
	for sup in supers:
		try:
			address = sup.a.contents[0]
		except:
			continue
		href = sup.a['href']
		d = req.get("http://www.lenta.com{}".format(href))
		d.encoding = "utf-8"
		text = re.sub(r'\&ndash;', '', d.text)
		sched_info = re.findall(r'Режим работы[^;]*;', text)
		schedule = ''
		if len(sched_info) > 0:
			schedule = sched_info[0]
			schedule = re.sub(r'<.*>', '', schedule)
		shop = BeautifulSoup(d.text, "lxml")
		blue2 = shop.find_all(class_="blue2")
		if len(blue2) > 0:
			blue2 = blue2[0]
			comment = blue2.strong.contents[0]
		else:
			blue2 = ''
			comment = ''
		
		
		row = []
		row.append(city)
		row.append(address)
		row.append(comment)
		row.append(schedule)
		row.append('')
		row.append('Лента')


		with open('data.csv', 'a') as file:
			wr = csv.writer(file, dialect='excel', delimiter=';')
			wr.writerow(row)
			file.close()


def parse():
	r = req.get("http://www.lenta.com/")
	r.encoding = "utf-8"
	soup = BeautifulSoup(r.text, "lxml")
	cities_info = re.findall(r"myAllTownInfo\['\w{1,10}'\]=[^;]*;", r.text)
	for city in cities_info:
		city_arr = re.findall(r'\[[^\[\]]+\]', city)
		lst = eval(city_arr[1])
		link = lst[1]
		city = lst[2]
		
		giper(link, city)
		time.sleep(0.1)
		super(link, city)
		time.sleep(0.1)

	
		
	'''with open('data.csv', 'a') as file:
			wr = csv.writer(file, dialect='excel', delimiter=';')
			wr.writerow(row)
			file.close()'''
		
		

if __name__ == "__main__":
	parse()