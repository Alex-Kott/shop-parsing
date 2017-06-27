import requests as req
from bs4 import BeautifulSoup
import re
import csv
import time



def parse():
	r = req.get("https://www.korablik.ru")
	r.encoding = "utf-8"
	
	
	cookies = r.cookies
	params = {
		'Accept' 			: 'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding' 	: 'gzip, deflate, br',
		'Accept-Language' 	: 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4,bg;q=0.2',
		'Connection' 		: 'keep-alive',
		'Host'				: 'www.korablik.ru',
		'Referer'			: 'https://www.korablik.ru/search/shops?search=&city=10136',
		'User-Agent'		: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
		'X-Requested-With'	: 'XMLHttpRequest'		
	}
	s = req.get("https://www.korablik.ru/shop-json?id=11464&scope=search&search=", cookies=cookies, params=params)
	print(s.text)
		
	'''with open('data.csv', 'a') as file:
								wr = csv.writer(file, dialect='excel', delimiter=';')
								wr.writerow(row)
								file.close()'''
		
		

if __name__ == "__main__":
	parse()