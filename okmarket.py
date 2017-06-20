import requests as req
from bs4 import BeautifulSoup
import csv

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
		soup = BeautifulSoup(r.text, "lxml")
		items = soup.find_all(class_="shop_list_item")
		




if __name__ == "__main__":
	parse()