# -*- utf-8 -*-
import sys, re, os, requests, json
import time, pprint
from http_request import *
from models import *


class Gome():

	iphone_list = [
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Gold', 'tag': '1123340454'},
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Rose Gold', 'tag': '1123340458'},
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Black', 'tag': '1123340507'},
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Silver', 'tag': '1123340456'},

		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Jet Black', 'tag': '1123340514'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Gold', 'tag': '1123340530'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Rose Gold', 'tag': '1123340529'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Black', 'tag': '1123340508'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Silver', 'tag': '1123340528'},

		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Jet Black', 'tag': '1123340527'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Gold', 'tag': '1123340535'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Rose Gold', 'tag': '1123340534'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Black', 'tag': '1123340531'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Silver', 'tag': '1123340512'},
	]

	def get_price(self, tag):
		ret = 0
		c = wget('http://item.gome.com.cn/9134401079-%s.html' % (tag))
		if c:
			m = re.search('gomePrice:\"(.*?)\"', c)
			if m:
				ret = m.group(1)
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
			ip.vendorid = 2
			ip.new()

def main():
	for x in iphone_list:
		print "{'memory': '%s', 'color': '%s', 'price': '%s'}," % (x['memory'], x['color'], get_price(x['tag']))


if __name__ == '__main__':
	main()