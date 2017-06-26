import requests as req
from bs4 import BeautifulSoup
import re
import csv


	
def parse():
	r = req.get("http://www.eldorado.ru/info/shops/cities/")
	soup = BeautifulSoup(r.text, "lxml")
	cities = soup.find_all(class_="vacancy_item")
	for i in cities:
		city = i.a.contents[0]
		href = i.a['href']
		s = req.get("http://www.eldorado.ru{}".format(href))
		shops_page = BeautifulSoup(s.text, "lxml")
		shops = shops_page.find_all(class_="shop-item")
		for i in shops:
			a = i.find('a')
			comment = a.contents[0]
			t = req.get("http://www.eldorado.ru{}".format(a['href']))
			shop = BeautifulSoup(t.text, "lxml")
			details = shop.find_all(class_="shop_detail_new")
			table = details[0].table
			trs = table.find_all('tr')
			tds = trs[0].find_all('td')
			address = re.sub(r'<[^<>]*>', '', str(tds[0]))
			address = re.sub(r'\s{2,}', '', address)

			phone = re.sub(r'<[^<>]*>', '', str(tds[1]))
			phone = re.sub(r'\s{2,}', '', phone)

			tds = trs[1].find_all('td')
			schedule = re.sub(r'<[^<>]*>', '', str(tds[1]))
			schedule = re.sub(r'\s{2,}', '', schedule)

			row = []
			row.append(city)
			row.append(address)
			row.append(comment)
			row.append(schedule)
			row.append(phone)
			row.append("Эльдорадо")

			with open('data.csv', 'a') as file:
				wr = csv.writer(file, dialect='excel', delimiter=';')
				wr.writerow(row)
				file.close()

		#print(i.a['href'])
	
		
	'''with open('data.csv', 'a') as file:
											wr = csv.writer(file, dialect='excel', delimiter=';')
											wr.writerow(row)
											file.close()'''
		
		

if __name__ == "__main__":
	parse()