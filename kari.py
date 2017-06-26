import requests as req
from bs4 import BeautifulSoup
import re
import csv


	
def parse():
	r = req.get("https://raw.githubusercontent.com/Alex-Kott/shop-parsing/master/content/kari.html");
	soup = BeautifulSoup(r.text, 'lxml')
	shop_list = soup.find(id="shop_list_all")
	
	for li in shop_list:
		row = []
		li = str(li)
		li = BeautifulSoup(li, "lxml")
		line_title = li.find_all(class_="sa_line_title")
		if len(line_title) == 0:
			continue
		title = str(line_title[0].contents[0])
		city_arr = title.split(",")
		city = city_arr[-1]
		city_arr = city_arr[:-1]
		comment = ", ".join(city_arr)
		comment += ""


		line_address = li.find_all(class_="sa_line_address")[0]
		address = line_address.contents[0]
		address = re.sub(r'\s{2,}', ' ', address)
		
		line_time = li.find_all(class_="sa_line_time")[0]
		schedule = line_time.contents[0]

		row.append(city)
		row.append(address)
		row.append(comment)
		row.append(schedule)
		row.append("")
		row.append("Кари")
		with open('data.csv', 'a') as file:
			wr = csv.writer(file, dialect='excel', delimiter=';')
			wr.writerow(row)
			file.close()



if __name__ == "__main__":
	parse()