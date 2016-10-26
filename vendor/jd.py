# -*- utf-8 -*-
import sys, re, os, requests, json
import time, pprint
from http_request import *
from models import *

class JD():

	iphone_list = [
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Gold', 'tag': 'J_3133811'},
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Rose Gold', 'tag': 'J_3133813'},
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Black', 'tag': 'J_3133817'},
		{'age': 7, 'model': 'A1660', 'memory': '32G', 'color': 'Silver', 'tag': 'J_3133815'},

		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Jet Black', 'tag': 'J_3133829'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Gold', 'tag': 'J_3133821'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Rose Gold', 'tag': 'J_3133823'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Black', 'tag': 'J_3133827'},
		{'age': 7, 'model': 'A1660', 'memory': '128G', 'color': 'Silver', 'tag': 'J_3133825'},

		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Jet Black', 'tag': 'J_3133839'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Gold', 'tag': 'J_3133831'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Rose Gold', 'tag': 'J_3133833'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Black', 'tag': 'J_3133837'},
		{'age': 7, 'model': 'A1660', 'memory': '256G', 'color': 'Silver', 'tag': 'J_3133835'},
	]

	def get_price(self, tag):
		ret = 0
		c = wget('http://p.3.cn/prices/mgets?callback=jQuery807689&type=1&area=&pdtk=&pduid=&pdpin=&pdbp=0&skuIds=%s' % (tag))
		if c:
			m = re.search('jQuery807689\((.*)\);', c)
			if m:
				try:
					page = json.loads(m.group(1))
					ret = page[0].get('p')
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
			ip.vendorid = 1
			ip.new()

def main():

	jd = JD()
	jd.fetchAll()
	#for x in iphone_list:
	#	print "{'memory': '%s', 'color': '%s', 'price': '%s'}," % (x['memory'], x['color'], get_price(x['tag']))


if __name__ == '__main__':
	if not os.path.exists(db_file):
		Base.metadata.create_all(engine)
	main()