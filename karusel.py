import requests as req
from bs4 import BeautifulSoup
import csv
import re
import json


def parse():
	r = req.get("http://karusel.ru/geo/places.js")
	response = r.text
	response = re.sub(r'^var placesJSON = ', '', response)
	response = re.sub(r'var plGroupedByCityJSO[\w|\W]*$', '', response)
	data = re.sub(r';\s{1,}$', '', response)
	print(json.loads(data, strict=False))
	
		




if __name__ == "__main__":
	parse()