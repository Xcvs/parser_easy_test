import requests
from bs4 import BeautifulSoup as bs
from random import choice, uniform
from time import sleep

headers = {'accept': '*/*', 
	    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4056.3 Safari/537.36'}

stable_url = 0
catalog_url = 0

def url_creater(stable_url, catalog_url):
	stable_url = 'https://www.srosa.ru/'
	catalog_url = 'voda/produktsija'
	base_url = stable_url + catalog_url
	print('Итоговая ссылка: ' + base_url)
	return base_url

base_url = url_creater(stable_url, catalog_url)

session = requests.Session()
request = session.get(base_url, headers=headers)

def card_discription(base_url):
	if request.status_code == 200:
		print('Code 2007')
		soup = bs(request.content, 'html.parser')
		pages = soup.find('div', attrs = {'class': 'blog-record-description'})
		contents = pages.text
		return contents
	else:
		print('Error')

def text(text):
	text = text.split('.')
	for i in text:
		print(i)
	


text(card_discription(base_url))	    


def list_menu(html):
	if request.status_code == 200:
		print('Code 2007')
		sleep(uniform(3,6))
		soup = bs(request.content, 'html.parser')
		pages = soup.find_all('ul', attrs = {'class': 'nav navbar-nav hidden-app'})
		for i in pages:
			try:
				print(i.text)
				drop_item = soup.find_all('a')
				print(drop_item.text)
			except:
				print('---')

	else:
		print('error')


list_menu(base_url)
