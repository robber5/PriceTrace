# -*- utf-8 -*-
import sys, re, os, requests, json
import time, pprint
from http_request import *
from models import *

class Suning():

	iphone_list = [
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Gold', 'tag': '000000000171958782'},
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Rose Gold', 'tag': '000000000171958781'},
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Black', 'tag': '000000000171958784'},
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Silver', 'tag': '000000000171958783'},

		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Jet Black', 'tag': '000000000171958785'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Gold', 'tag': '000000000171958788'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Rose Gold', 'tag': '000000000171958786'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Black', 'tag': '000000000171958790'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Silver', 'tag': '000000000171958789'},

		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Jet Black', 'tag': '000000000171958791'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Gold', 'tag': '000000000171958793'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Rose Gold', 'tag': '000000000171958792'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Black', 'tag': '000000000171958795'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Silver', 'tag': '000000000171958794'},
	]

	def get_price(self, tag):
		ret = 0
		c = wget('http://pas.suning.com/nspcsale_0_%s_%s_0000000000_10_010_0100101_20089_1000000_9017_10106_Z001.html?callback=pcData&_=1476757279303' % (tag, tag))
		if c:
			m = re.search('pcData\((.*)\)', c)

			if m:
				try:
					page = json.loads(m.group(1))
					price = page.get('data').get('price').get('saleInfo')
					ret = price[0].get('netPrice')
				except Exception as e:
					print e
		return ret

	def fetchAll(self):
		for x in self.iphone_list:
			price = 0
			for y in xrange(1,3):
				price = self.get_price(x['tag'])
				if price > 0:
					break

			#print "{'memory': '%s', 'color': '%s', 'price': '%s'}" % (x['memory'], x['color'], self.get_price(x['tag']))
			ip = Iphone()
			ip.age = x['age']
			ip.model = x['model']
			ip.color = x['color']
			ip.memory = x['memory']
			ip.price = price
			ip.vendorid = 3
			ip.new()

def main():
	for x in iphone_list:
		print "{'memory': '%s', 'color': '%s', 'price': '%s'}," % (x['memory'], x['color'], get_price(x['tag']))
#		print get_price(x['tag'])


if __name__ == '__main__':
	main()