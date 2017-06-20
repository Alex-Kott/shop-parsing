import korablik
import okmarket

try:
	korablik.parse()
	print("Korablik was parsed")
except:
	print("Korablik was not parsed")

try:
	okmarket.parse()
	print("Okmarket was parsed")
except:
	print("Okmarket was not parsed")