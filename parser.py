# -*- coding: utf-8 -*-
import csv
import korablik
import okmarket
import auchan
import karusel
import kari
import dochkisinochki
import atak
import eldorado
import lenta
import detmir


# город, адрес, коммент (название ТЦ, например), график работы, телефон, формат(?)
fields = ['Город', 'Адрес', 'Комментарий', 'График работы', 'Телефон', 'Магазин', 'Формат']
with open('data.csv', 'w') as file:
	wr = csv.writer(file, dialect='excel', delimiter=';')
	wr.writerow(fields)

'''
try:
	korablik.parse()
	print("Korablik was parsed")
except Exception as e:
	print("Korablik was not parsed")'''

try:
	okmarket.parse()
	print("Okmarket was parsed")
except Exception as e:
	print(str(e))
	print("Okmarket was not parsed")

try:
	auchan.parse()
	print("Auchan was parsed")
except Exception as e:
	print(str(e))
	print("Auchan was not parsed")

try:
	karusel.parse()
	print("Karusel was parsed")
except Exception as e:
	print(str(e))
	print("Karusel was not parsed")
	
try:
	kari.parse()
	print("Kari was parsed")
except Exception as e:
	print(str(e))
	print("Kari was not parsed")
	
try:
	dochkisinochki.parse()
	print("Dochkisinochki was parsed")
except Exception as e:
	print(str(e))
	print("Dochkisinochki was not parsed")
	
try:
	atak.parse()
	print("ATAK was parsed")
except Exception as e:
	print(str(e))
	print("ATAK was not parsed")
	
try:
	eldorado.parse()
	print("Eldorado was parsed")
except Exception as e:
	print(str(e))
	print("Eldorado was not parsed")
	
try:
	lenta.parse()
	print("Lenta was parsed")
except Exception as e:
	print(str(e))
	print("Lenta was not parsed")
	
try:
	detmir.parse()
	print("Detmir was parsed")
except Exception as e:
	print(str(e))
	print("Detmir was not parsed")



file.close()