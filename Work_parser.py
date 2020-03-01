import requests
from bs4 import BeautifulSoup as bs
from random import choice, uniform
from time import sleep


headers = {'accept': '*/*', 
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}


#mirror bullshit

print('Введите номер телефона:')
pfone = input()



def url_creater(pfone_number):
	stable_url = 'https://mirror.bullshit.agency/search_by_phone/'
	pfone_url = str(pfone)
	base_url = stable_url + pfone_url 
	return base_url

def info(base_url):
	session = requests.Session()
	request = session.get(base_url, headers=headers)
	if request.status_code == 200:
		print('Code 200 +')
		soup = bs(request.content, 'html.parser')
		items = soup.find_all('div', attrs = {'style': 'vertical-align: baseline'})
		hrefs = soup.find_all('a')
		print('Список ссылок с изображениями:')
		for link in hrefs:
			print('https://mirror.bullshit.agency'+link.get('href'))
		for item in items:
			try:
				print('----------------------------------------------------------------------------')
				item_heading = item.find('h4', attrs = {'class': 'media-heading'}).text
				item_discriptions = item.find('p')
				print(item_heading)
				print(item_discriptions.text)
			except:
				print('None')			
	else:
		print('Сервер не ответил качественным конектом')
	

info(url_creater(pfone))

#avinfo



