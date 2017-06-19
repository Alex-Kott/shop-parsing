import requests as req
from bs4 import BeautifulSoup

r = req.get("https://www.korablik.ru/shops");
soup = BeautifulSoup(r.text, 'lxml')
select = soup.find(id="country_id")
country_id = []
for option in select:
	try:
		country_id.append(option['value'])
	except:
		continue

for id in country_id:
	params = {'search' : '', 'city' : id}
	r = requests.get('www.korablik.ru/search/shops', params = params)
	
