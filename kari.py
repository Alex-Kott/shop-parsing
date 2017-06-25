import requests as req
from bs4 import BeautifulSoup
import re


	
def parse():
	r = req.get("https://raw.githubusercontent.com/Alex-Kott/shop-parsing/master/content/kari.html");
	soup = BeautifulSoup(r.text, 'lxml')
	shop_list = soup.find(id="shop_list_all")
	
	for li in shop_list:
		li = str(li)
		li = BeautifulSoup(li, "lxml")
		line_title = li.find_all(class_="sa_line_title")
		if len(line_title) == 0:
			continue
		#print(line_title[0].contents[0])
		title = str(line_title[0].contents[0])
		city_arr = re.findall(r',.*', title)
		if len(city_arr) == 0:
			city = title
		else:
			city = city_arr[0]
		print(city)
		
	


if __name__ == "__main__":
	parse()