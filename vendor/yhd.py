# -*- utf-8 -*-
import sys, re, os, requests, json
import time, pprint
from http_request import *
from models import *

class Yhd():

	iphone_list = [
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Gold', 'tag': '66315667'},
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Rose Gold', 'tag': '66315668'},
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Black', 'tag': '66315665'},
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Silver', 'tag': '66315669'},

		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Jet Black', 'tag': '66315648'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Gold', 'tag': '66315649'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Rose Gold', 'tag': '66315650'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Black', 'tag': '66315647'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Silver', 'tag': '66315651'},

		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Jet Black', 'tag': '66315657'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Gold', 'tag': '66315658'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Rose Gold', 'tag': '66315659'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Black', 'tag': '66315656'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Silver', 'tag': '66315660'},
	]

	def get_price(self, tag):
		ret = 0
		c = wget('http://gps.yhd.com/restful/detail?mcsite=1&provinceId=2&pmId=%s' % (tag))
		if c:
			try:
				page = json.loads(c)
				ret = page.get('currentPrice')
				#print price
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
			ip.vendorid = 4
			ip.new()

def main():
	pass
	#print get_price('66126405')

#	for x in iphone_list:
#		print "{'memory': '%s', 'color': '%s', 'price': '%s'}," % (x['memory'], x['color'], get_price(x['tag']))


if __name__ == '__main__':
	main()