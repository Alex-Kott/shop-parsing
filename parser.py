# -*- coding: utf-8 -*-
import csv
import korablik
import okmarket
import auchan
import karusel


# город, адрес, коммент (название ТЦ, например), график работы, телефон, формат(?)
fields = ['Город', 'Адрес', 'Комментарий', 'График работы', 'Телефон', 'Формат']
with open('data.csv', 'w') as file:
	wr = csv.writer(file, dialect='excel', delimiter=';')
	wr.writerow(fields)

'''
try:
	korablik.parse()
	print("Korablik was parsed")
except:
	print("Korablik was not parsed")'''

try:
	okmarket.parse()
	print("Okmarket was parsed")
except:
	print("Okmarket was not parsed")

try:
	auchan.parse()
	print("Auchan was parsed")
except:
	print("Auchan was not parsed")

try:
	karusel.parse()
	print("Karusel was parsed")
except:
	print("Karusel was not parsed")
	
try:
	karusel.parse()
	print("Karusel was parsed")
except:
	print("Karusel was not parsed")



file.close()