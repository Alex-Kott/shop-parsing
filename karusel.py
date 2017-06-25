import requests as req
from bs4 import BeautifulSoup
import csv
import re
import json

def detect_city(location):
	(lat,lng) = location.split(',')
	params = {
		'format'  : 'json',
		'geocode' : '{},{}'.format(lng,lat)
	}
	geocode = req.get("https://geocode-maps.yandex.ru/1.x/", params=params)
	geo_member = geocode.json()['response']['GeoObjectCollection']['featureMember']
	geo_obj = geo_member[0]['GeoObject']
	city = geo_obj['description']
	return city



def parse():
	r = req.get("http://karusel.ru/geo/places.js")
	response = r.text
	response = re.sub(r'^var placesJSON = ', '', response)
	response = re.sub(r'var plGroupedByCityJSO[\w|\W]*$', '', response)
	content = re.sub(r';\s{1,}$', '', response)
	data = json.loads(content, strict=False)
	places = data['places']
	place = places['place']
	
	for i in place:
		row = []
		comment = i['title']
		address = i['address']
		city = detect_city(i['location'])
		schedule = i['schedule']
		phone = i['telephone']
		format_ = ''

		row.append(city)
		row.append(address)
		row.append(comment)
		row.append(schedule)
		row.append(phone)
		row.append(format_)
		with open('data.csv', 'a') as file:
			wr = csv.writer(file, dialect='excel', delimiter=';')
			wr.writerow(row)
	
		file.close()
	
		
if __name__ == "__main__":
	parse()