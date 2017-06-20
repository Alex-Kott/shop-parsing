import requests as req
from bs4 import BeautifulSoup


	
def parse():
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
		#params = {'search' : '', 'city' : 10127}
		request = req.get('https://www.korablik.ru/search/shops', params = params)
		cookies = req.utils.dict_from_cookiejar(request.cookies)
		print(cookies)

		params = {'search' : '', 'scope' : 'search', 'id' : id}
		headers = {	'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3128.3 Safari/537.36',
					'Referer' : 'https://www.korablik.ru/search/shops?city={}&search='.format(id),
					'Accept' : 'application/json, text/javascript, */*; q=0.01',
					'Accept-Encoding' : 'gzip, deflate, br',
					'Accept-Language' : 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
					'Host' : 'www.korablik.ru'}
		page = req.get('https://www.korablik.ru/shop-json', params = params, cookies = cookies, headers = headers)
		city = BeautifulSoup(page.text, "lxml")
		#print(page.text)
		#shops = city.find_all('div', class_="_items_count_seach_reg")


if __name__ == "__main__":
	parse()