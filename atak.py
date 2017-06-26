import requests as req
from bs4 import BeautifulSoup
import re
import csv


	
def parse():
	r = req.get("http://www.ataksupermarket.ru/shops/")
	soup = BeautifulSoup(r.text, "lxml")
	selects = soup.find_all("select")
	select = selects[1]
	for option in select:
		str_option = str(option)
		if len(str_option) == 1:
			continue
		opt = BeautifulSoup(str_option, "lxml")
		city = option.contents[0]
		with open("test.txt", 'a') as f:
			f.write(city+"\n")
		f.close()
		if city == "Выбор города":
			continue
		link = option['link']
		s = req.get('http://www.ataksupermarket.ru{}'.format(link))
		pms = re.findall(r'var pm = .*;', s.text)
		for pm in pms:
			div = re.findall(r'<div>.*<\/div>', pm)[0]
			info = div.split('<br  />')
			phone = re.findall(r'<a.*>[+\s0-9\(\)]*<\/a>', info[-1])
			if len(phone) == 0:
				phone = ''
			else:
				phone = re.sub(r'<[^<>]*>', '', phone[0])
			address = re.sub(r'<[^<>]*>', '', info[0])

			schedule = re.findall(r'Режим работы:[^<>]*', div)
			if len(schedule) > 0:
				schedule = schedule[0]
			comment = ""

			row = []
			row.append(city)
			row.append(address)
			row.append(comment)
			row.append(schedule)
			row.append(phone)
			row.append("АТАК")
		
			with open('data.csv', 'a') as file:
				wr = csv.writer(file, dialect='excel', delimiter=';')
				wr.writerow(row)
				file.close()
		
		

if __name__ == "__main__":
	parse()