import requests as req
from bs4 import BeautifulSoup
import re
import csv
import time

def section(sect):
	s = req.get("http://magnit-info.ru/buyers/adds/list.php?SECTION_ID={}".format(sect))
	cookies = s.cookies
	page = BeautifulSoup(s.text, "lxml")
	for regid in region:
		reg_cities = page.find(id='region_{}'.format(regid))
		links = reg_cities.find_all("a")
		for a in links:
			cid = re.findall(r'\(\d+\)', a['href'])[0]
			cid = cid[1:-1]
			city = a.contents[0]

			#получим куки
			for_cookies = req.get("http://magnit-info.ru/buyers/adds/ajax.php")
			cookies = for_cookies.cookies
			params = {
				'op' : 'get_shops',
				'SECTION_ID' : sect,
				'RID' : regid,
				'CID' : cid
			}

			headers = {
				"Accept" 			: "application/json, text/javascript, */*; q=0.01",
				"Host" 				: "magnit-info.ru",
				"Origin"			: "http://magnit-info.ru",
				"Referer"			: for_cookies.url,
				"User-Agent"		: "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
				"X-Requested-With" 	: "XMLHttpRequest"

			}

			headers = {
				"Host" : " magnit-info.ru",
				"Connection" : " keep-alive",
				"Content-Length" : " 22",
				"Origin" : " http://magnit-info.ru",
				"User-Agent" : " Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
				"Content-Type" : " application/x-www-form-urlencoded",
				"Accept" : " application/json, text/javascript, */*; q=0.01",
				"X-Requested-With" : " XMLHttpRequest",
				"Accept-Encoding" : " gzip, deflate",
				"Accept-Language" : " ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4,bg;q=0.2",
				"Cookie" : " PHPSESSID=9n5ah2kd62shc6nnk4ncrnpn27; _ym_uid=1498825757118568292; _ym_isad=1; BITRIX_SM_mycity=19822670; BITRIX_SM_myreg=25; _ga=GA1.2.592745248.1498825755; _gid=GA1.2.786414773.1498825755; _ym_visorc_9726625=w"
							
			}



			t = req.get("http://magnit-info.ru/functions/bmap/func.php", params = params, cookies = cookies)
			#print(t.url)
			print(t.text)




def parse():

	gip = 1257 # это для гипермаркетов
	sup = 1258 # это для универсамов (супермаркетов)
	r = req.get("http://magnit-info.ru/")
	soup = BeautifulSoup(r.text, "lxml")
	select_region = soup.find_all(class_="select_region")[0]
	tds = select_region.find_all("td")
	for td in tds:
		divs = td.find_all("div")
		for div in divs:
			a = div.a
			reg = a.contents[0]
			try:
				regid = re.findall(r'\(\d+\)', a['onclick'])[0]
				regid = regid[1:-1]
			except:
				regid = re.findall(r'\(\d+,', a['href'])[0]
				regid = regid[1:-1]
			region[regid] = reg
	section(gip)
	section(sup)




		
'''with open('data.csv', 'a') as file:
							wr = csv.writer(file, dialect='excel', delimiter=';')
							wr.writerow(row)
							file.close()'''
		

region = dict()	

if __name__ == "__main__":
	parse()