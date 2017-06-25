import requests as req
from bs4 import BeautifulSoup
import csv
import re

city_links = []



def parse():
	
	r = req.get("https://www.auchan.ru/ru/")
	soup = BeautifulSoup(r.text, "lxml")
	sections = soup.find_all(class_="f-section")
	cities = sections[0].ul
	for li in cities:
		a = li.find('a')
		if a != -1:
			link = []
			if a['href'] == '/ru/pokupki': # ссылку на Ашан Интернет-магазин пропускаем
				continue
			link.append(a.contents[0])
			link.append(a['href'])
			city_links.append(link)
	for l in city_links:
		r = req.get("https://www.auchan.ru{}".format(l[1]))
		soup = BeautifulSoup(r.text, "lxml")
		shop_lists = soup.find_all(class_="shops-list")
		if len(shop_lists) == 0:
			content = soup.find_all(class_="contentRightBox")[0]
			ps = content.find_all('p')
			row = []
			row.append(l[0])
			address = ''
			comment = 'Ашан'
			schedule = ''
			phone = ''
			format_ = ''
			for p in ps:
				p = p.text
				flag = False
				if p.find('Адрес') != -1:
					flag=True
				if p.find('Режим') != -1:
					flag=True
				if p.find('Телефон') != -1:
					flag=True
				if flag:
					info = p.split('\n\n')
					
					for i in info:
						if i.find('Адрес') != -1:
							address = re.sub(r'Адрес[\w|\W]*:', '', i)
							address = re.sub(r'Адрес', '', address)
							address = re.sub(r';', '', address)
							address = re.sub(r'\n', '', address)
						if i.find('Режим') != -1:
							schedule = re.sub(r'Режим работы:', '', i)
							schedule = re.sub(r'Режим работы', '', schedule)
							schedule = re.sub(r';', '', schedule)
							schedule = re.sub(r'\n', '', schedule)
						if i.find('Телефон') != -1:
							phone = re.sub(r'Телефон[\w|\W]*:', '', i)
							phone = re.sub(r'Телефон', '', phone)
							phone = re.sub(r';', '', phone)
							phone = re.sub(r'\n', ', ', phone)
							
			row.append(address)
			row.append(comment)
			row.append(schedule)
			row.append(phone)
			row.append(format_)
			with open('data.csv', 'a') as file:
				wr = csv.writer(file, dialect='excel', delimiter=';')
				wr.writerow(row)
				file.close()

		else:
			for shop_list in shop_lists:
				lis = shop_list.find_all('li')
				for li in lis:
					row = []
					row.append(l[0])

					strong = li.find('strong')
					try:
						a = strong.find('a')
						comment = a.contents[0]
						href = a['href']
						point_page = req.get("https://www.auchan.ru{}".format(href))
						inf = BeautifulSoup(point_page.text, "lxml")
						content = inf.find_all(class_="contentRightBox")[0]
						ps = content.find_all('p')
						row = []
						row.append(l[0])
						address = ''
						comment = 'Ашан'
						schedule = ''
						phone = ''
						format_ = ''
						for p in ps:
							p = p.text
							flag = False
							if p.find('Адрес') != -1:
								flag=True
							if p.find('Режим') != -1:
								flag=True
							if p.find('Телефон') != -1:
								flag=True
							if flag:
								info = p.split('\n\n')
								
								for i in info:
									if i.find('Адрес') != -1:
										address = re.sub(r'Адрес[\w|\W]*:', '', i)
										address = re.sub(r'Адрес', '', address)
										address = re.sub(r';', '', address)
										address = re.sub(r'\n', '', address)
									if i.find('Режим') != -1:
										schedule = re.sub(r'Режим работы:', '', i)
										schedule = re.sub(r'Режим работы', '', schedule)
										schedule = re.sub(r';', '', schedule)
										schedule = re.sub(r'\n', '', schedule)
									if i.find('Телефон') != -1:
										phone = re.sub(r'Телефон[\w|\W]*:', '', i)
										phone = re.sub(r'Телефон', '', phone)
										phone = re.sub(r';', '', phone)
										phone = re.sub(r'\n', ', ', phone)
										phone = phone.strip([', '])
						if address == '':
							continue
						row.append(address)
						row.append(comment)
						row.append(schedule)
						row.append(phone)
						row.append(format_)
						#print(row)
						with open('data.csv', 'a') as file:
							wr = csv.writer(file, dialect='excel', delimiter=';')
							wr.writerow(row)
							file.close()
					except:
						a = 1
					


if __name__ == "__main__":
	parse()