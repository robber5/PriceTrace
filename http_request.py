# -*- utf-8 -*-
import sys, re, os, requests
import time

proxies = {"http": "web-proxy.oa.com:8080",}
#headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"}
#treatyPackageId=729&fuzzyPhoneNum=

#proxies = {}
headers = {}
cookies = {}
#cookies = {"Cookie": "Hm_lvt_cb12e33a15345914e449a2ed82a2a216=1472626125; sesab=a; sesabv=56%23100%3A0; SN_CITY=10_010_1000000_9017_01_10106_2_0; cityId=9017; districtId=10106; _device_session_id=p_424da5e3-e7e5-4fec-bcd9-25b906d349de; WC_SERVER=1; smhst=200132356a200153354a200178897; _snsr=direct%7Cdirect%7C%7C%7C; __wmv=1472626122.5; _gat=1; authId=siB0A9B57391C91DF06774BB45DEB0BB24; __snuotr=2EF8B5000KV2%26HCA7GGDFAK1%24K4161UIU%3DF%24D5; custno=5203510265; idsLoginUserIdLastTime=robber5%40live.com; logonStatus=2; nick=Robber5...; nick2=Robber5...; _snma=1%7C147262612224611401%7C1472626122246%7C1475225092917%7C1475225097434%7C26%7C5; _snmc=1; _snmp=147522509716991474; _snmb=147522509292083356%7C1475225097489%7C1475225097436%7C2; _snms=147522509748969132; __ssaf=http%3A%2F%2Fsearch.suning.com%2F%25E8%2581%2594%25E9%2580%259A%25E6%2589%258B%25E6%259C%25BA%25E5%258D%25A1%2F; __ssar=direct%7Cdirect%7C%7C%7C; __ssav=147262612224611401%7C1472626134219%7C1475041249433%7C1475225097719%7C5%7C4%7C0; __ssas=147522509772283203%7C1475225097725%7C1475225097722%7C1; _ga=GA1.2.1828489426.1472626124; _cusenoek=157954B25062EE75ABDA4IDW"}
#headers = {"X-Log-Uid": "3254894593", "User-Agent": "Weibo/5934 (iPhone; iOS 7.1.1; Scale/2.00)"}
#cookies = {"Cookie": "gsid_CTandWM=4uC941c81NYIcrhEvefy6dEKi9z; SUB=_2A257cXdzDeThGeVM7lYZ-SrJwj-IHXVY7SM7rDV9PUJbr9AKLRTxkWtwlUbhjLCfpsU0iLXP_rBo34GXlw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWF676UK1fPBfDLhXa5p3q6"}

def wget(url):

	output =  None

	try:
		s = requests.Session()
		r = s.get(url, proxies=proxies, headers = headers, cookies = cookies, verify=False)

		if r.status_code == requests.codes.ok:
			output = r.content
			#print r.__dict__
	except Exception, e:
		print(e)

	return output


def wpost(url, payloads):

	output =  None

	try:
		s = requests.Session()
		r = s.post(url, proxies=proxies, headers = headers, data = payloads, verify=False)

		if r.status_code == requests.codes.ok:
			output = r.content
	except Exception, e:
		print(e)

	return output


def main():
#	c = wget('https://www.amazon.cn/dp/B01LX5KR6D/ref=twister_B01LYT5NA7?_encoding=UTF8&amp;psc=1')
	c = wget('http://pas.suning.com/nspcsale_0_000000000171958792_000000000171958792_0000000000_10_010_0100101_20089_1000000_9017_10106_Z001.html?callback=pcData&_=1476757279303')
	print c
#	c = wget('http://www.weibo.com')
	#c = wpost('https://zhenwifi.kf0309.3g.qq.com/?rid=2927493387', '\{"method":"getpwd","mac":"74:51:ba:c9:39:24"\}');
	#c = wpost('http://localhost/cgi-bin/registor/reg.cgi', 'ssid=Tencent_Beijing&bssid=74:51:ba:c9:39:24');
	#c = wpost('http://localhost/cgi-bin/registor/reg.cgi', '{ssid}');





if __name__ == '__main__':
	main()