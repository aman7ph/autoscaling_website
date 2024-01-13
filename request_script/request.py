from multiprocessing import Pool
from request import get

DOMAIN=''

def send_request(val):
	while True:
		response=get(f'http://{DOMAIN}')
		data=response.json()
		print('Sent request')
		print(data)
