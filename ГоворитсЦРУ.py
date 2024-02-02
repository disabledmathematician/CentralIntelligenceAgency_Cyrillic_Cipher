import urllib3

def talktoCIA_charlescarltruscott():
	http = urllib3.PoolManager()
	resp = http.request('GET', 'https://www.cia.gov')
	print(resp.data)
	print(resp.headers)
talktoCIA_charlescarltruscott()