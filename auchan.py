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
		row = []
		row.append(l[0])
		
		r = req.get("https://www.auchan.ru{}".format(l[1]))
		soup = BeautifulSoup(r.text, "lxml")
		shop_lists = soup.find_all(class_="shops-list")
		if len(shop_lists) == 0:
			print("single shop")
		else:
			for shop_list in shop_lists:
				for li in shop_list:
					print(li)

	
		




if __name__ == "__main__":
	parse()