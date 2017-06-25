import requests as req
from bs4 import BeautifulSoup


	
def parse():
	r = req.get("https://www.korablik.ru/shops");
	soup = BeautifulSoup(r.text, 'lxml')
	


if __name__ == "__main__":
	parse()