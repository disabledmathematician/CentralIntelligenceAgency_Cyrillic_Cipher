import numpy as np
import pandas as pd
import urllib3
# Charles Truscott Watters
import base64
import datetime

def ЦРУ():
	http = urllib3.PoolManager()
	resp = http.request('GET', 'https://www.cia.gov')
#	print(resp.data)
	id = dict(resp.headers)['ID']
	session = dict(resp.headers)['SESSION']
	print(id)
	did = base64.b64decode(id)
	print(str(did))
	dt = str(datetime.datetime.now())
	date = dt.split(' ')[0]
	time = str(datetime.datetime.now()).split(' ')[1]
	time = time.split(':')
	time = time[0] + time[1]
	file = open('{}.txt'.format(str(date + time)), 'w')
#	decode = did.decode('utf-8')
	s = str(did, 'utf-16')
#	for e in decode:
#		s += ord(e)
	file.write(s)
	file.write(" ")
	file.write(str(datetime.datetime.now()))
	file.write(" ")
	file.write("Central Intelligence Agency. Charles Truscott")
	file.close()
	
#	print(bytes(did))
ЦРУ()