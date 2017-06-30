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
			params = {
				'op' : 'get_shops',
				'SECTION_ID' : sect,
				'RID' : regid,
				'CID' : cid
			}
			t = req.get("http://magnit-info.ru/functions/bmap/func.php", params = params, cookies = cookies)
			print(t.url)
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