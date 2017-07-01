import requests as req
from bs4 import BeautifulSoup
import re
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

			url = "http://magnit-info.ru/buyers/adds/{}/{}/{}".format(sect, regid, cid)

			
			driver.get(url)
			time.sleep(3)
			elems = []
			try:
				elem = driver.find_element_by_class_name("addresses")
				element = elem.get_attribute('innerHTML')
			except:
				continue

			tbody = BeautifulSoup(element, "lxml")

			trs = tbody.find_all("tr")
			del trs[0]
			for tr in trs:
				tds = tr.find_all("td")
				location = tds[1].a.contents[0]
				location = re.sub(r'^\d+,', '', str(location))
				try:
					city = re.findall(r'(.*\s(г|с|п|пгт|д|аул),)', location)[0][0]
					address = location.replace(city, '')
					city = city.strip(',')
				except:
					address = location
					city = location

				schedule = tds[2].contents[0]
				if sect == 1258:
					format_ = "Гипермаркет"
				else:
					format_ = "Супермаркет"
				row = []
				row.append(city)
				row.append(address)
				row.append("")
				row.append(schedule)
				row.append("")
				row.append("Магнит")
				row.append(format_)

				with open('magnit.csv', 'a') as file:
					wr = csv.writer(file, dialect='excel', delimiter=';')
					wr.writerow(row)
					file.close()
			






def parse():

	with open('magnit.csv', 'w') as file: # подготовим файлик очистив его перед записью
		wr = csv.writer(file, dialect='excel', delimiter=';')
		file.close()

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
	section(sup)

	section(gip)



		
'''with open('data.csv', 'a') as file:
							wr = csv.writer(file, dialect='excel', delimiter=';')
							wr.writerow(row)
							file.close()'''
		

region = dict()	
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("/home/alexkott/Documents/YouDo/shop-parsing/selenium_test/chromedriver", chrome_options=options)


if __name__ == "__main__":
	parse()
	driver.quit()