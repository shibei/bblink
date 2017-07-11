#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-05 20:48:24
# @Author  : mx (shibei1988@foxmail.com)
# @Link    : 
# @Version : $Id$
import requests,json,time,xlwt,xlrd


def getData(url_1):
	re=requests
	hc=re.get(url=url_1)
	data=hc.text
	data=json.loads(data)
	return data

circulate,row=1,0

w=xlwt.Workbook()
api_url='http://gbcom.hos-wifi.com:8888/ccsv3/rest/partner/bblink/routers'
data=getData(api_url)['data']
title=['time']+[x for x in data[0]]
for sheets in data:
	ws=w.add_sheet(sheets['gwid'])
	for mtitle in title:
		ws.write(0,row,mtitle)
		row=row+1 
	row=0

while True:
	api_url='http://gbcom.hos-wifi.com:8888/ccsv3/rest/partner/bblink/routers'

	data=getData(api_url)['data']

	# ws=w.add_sheet('test')
	mtime=time.strftime('%Y-%m-%d-%H:%M',time.localtime(time.time()))
	print(mtime)
	# print(title)


	# print(dict({'time' : mtime},**data[0]))
	for line in data:
		wss=w.get_sheet(line['gwid'])
		line=dict({'time' : mtime},**line)
		for v in line:
			wss.write(circulate,row,line[v])
			row=row+1
		row=0

	circulate=circulate+1
	w.save('C:\\Users\\chen\\Documents\\python\\test.xls') 
	time.sleep(600)
	