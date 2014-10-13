#!/usr/bin/python
#-*-coding:utf-8-*-
"""
url = "https://api.foursquare.com/v2/venues/search?"
LIMIT = "limit=" + "50&"
VERSION = "v=" + "20140913&"
CATEGORYID = "categoryId=" + "4d4b7105d754a06374d81259&"
INTENT = "intent=" + "browse&"
SW = "sw=" + "35.690060,139.700197&"
NE = "ne=" + "35.705534,139.721140"
"""
"""
TOTAL_URL = "https://api.foursquare.com/v2/venues/search?limit=50&client_id=K0KKIRDEKPIYE3MYCPTT4NMQYTBQ2XK5CA0TQDZU04BDOU54&client_secret=CO42NEHS5QWDBU10ZQJPLBG02VUZDYDT33H3DLX2QEJKYPG1&v=20140913&categoryId=4d4b7105d754a06374d81259&intent=browse&sw=35.690060,139.700197&ne=35.705534,139.721140"
"""
"""
response = urllib2.urlopen(\
	"https://api.foursquare.com/v2/venues/search?"\
	"limit=50&"\
	"client_id=K0KKIRDEKPIYE3MYCPTT4NMQYTBQ2XK5CA0TQDZU04BDOU54&"\
	"client_secret=CO42NEHS5QWDBU10ZQJPLBG02VUZDYDT33H3DLX2QEJKYPG1&"\
	"v=20140913&"\
	"categoryId=4d4b7105d754a06374d81259&"\
	"intent=browse&"\
	"sw=35.690060,139.700197&"\
	"ne=35.705534,139.721140"\
	)
"""
"""
渋谷駅
swlatitude = 35.657692
swlongitude = 139.699406

nelatitude = 35.658224
nelongitude = 139.699771
"""
"""
アフガニスタン料理店 = 503288ae91d4c4b30a586d67
アフリカ料理店 = 4bf58dd8d48988d1c8941735
アメリカ料理店 = 4bf58dd8d48988d14e941735
ベネゼエラ料理店 = 4bf58dd8d48988d152941735
アルゼンチン料理店 = 4bf58dd8d48988d107941735
アジア料理店 = 4bf58dd8d48988d142941735
オーストラリア料理店 = 4bf58dd8d48988d169941735
オーストリア料理店 = 52e81612bcbc57f1066b7a01
焼肉/BBQ = 4bf58dd8d48988d1df931735
ベーグルショップ = 4bf58dd8d48988d179941735
パン屋 = 4bf58dd8d48988d16a941735
ベラルーシ料理店 = 52e928d0bcbc57f1066b7e97
"""
import urllib2
import simplejson
import json
import urllib
import time
"""
swlatitude = float(35.657692)
swlongitude = float(139.700197)
nelatitude = float(35.658224)
nelongitude = float(139.721140)
"""
class VenueCollect:
	def __init__(self):
		print "START"

	def venues(self, urldic, swlatitude, swlongitude, nelatitude, nelongitude):
		count = 0
		out_of_range = 0
		"""東京の左下から東京の右上まで"""
		for Ydirection in range (1,400):
			c = swlatitude
			d = nelatitude
			swlatitude = d
			nelatitude = d*2 - c
			for Xdirection in range(1,30):
				"""右端まで四角形を異動"""
				SW = "&sw=" + str(swlatitude) + "," + str(swlongitude) + "&"
				NE = "ne=" + str(nelatitude) + "," + str(nelongitude)
				params = urllib.urlencode(urldic)
				response = urllib2.urlopen(url+params+SW+NE)
				data = json.load(response)
				a = swlongitude
				b = nelongitude
				#print type(swlongitude),type(nelongitude)
				swlongitude = b
				nelongitude = b*2 - a
				shop_number_count = 0
				print "swlongitude = ",swlongitude
				print "nelongitude = ",nelongitude
				print "swlatitude = ",swlatitude
				print "nelatitude = ",nelatitude
				for i in data['response']['venues']:
					#print i['name']
					#print i['categories'][0]['pluralName']
					#print i['categories'][0]['id']
					#print i['location']['lat']
					#print i['location']['lng']
					shop_number_count += 1
					if shop_number_count == 50:
						out_of_range += 1
					time.sleep(5)
				print shop_number_count
				count += 1
				print "count = ",count
				print
				#print count,type(swlatitude)
		#print type(urldic['limit'])
if __name__ == '__main__':
	url = "https://api.foursquare.com/v2/venues/search?"
	urldic = {'limit':50,
	'client_id':'???',
	'client_secret':'???',
	'v':'20140913',
	'categoryId':'4d4b7105d754a06374d81259',
	'intent':'browse',}
	swlatitude = float(35.632496)
	swlongitude = float(139.259285)
	nelatitude = float(35.633028)
	nelongitude = float(139.280228)
	#vc = VenueCollect()
	#vc.venues(urldic, swlatitude, swlongitude, nelatitude, nelongitude)
	VenueCollect().venues(urldic, swlatitude, swlongitude, nelatitude, nelongitude)
	"""
	StartPoint(\
	float(35.690060), float(139.700197),\
	float(35.705534), float(139.721140)\
	)
	"""


