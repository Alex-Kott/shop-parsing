import requests as req
from bs4 import BeautifulSoup
import re
import csv


	
def parse():
	r = req.get("http://www.dochkisinochki.ru/ajax/shops_getList.php");
	#json = r.json(strict=False)
	print(r.status_code)

	'''
	with open('data.csv', 'a') as file:
		wr = csv.writer(file, dialect='excel', delimiter=';')
		wr.writerow(row)
		file.close()'''



if __name__ == "__main__":
	parse()