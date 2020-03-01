import requests
from bs4 import BeautifulSoup as bs
from random import choice, uniform
from time import sleep


headers = {'accept': '*/*', 
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}

print('Введите номер телефона:')
pfone = input()

def url_creater_avinfo(pfone_number):
	stable_url = 'https://avinfo.guru/info/?phone='
	pfone_url = str(pfone[1:])
	base_url = stable_url + pfone_url
	return base_url

def info_avinfo(base_url):
	session = requests.Session()
	request = session.get(base_url, headers=headers)
	if request.status_code == 200:
		print('Code 200 +')
		print()
		soup = bs(request.content, 'html.parser')
		items = soup.find('div', attrs = {'class': 'alert alert-warning fade in alert-dismissable'})
		a = items.find_all('a')
		for i in a:
			print(i.text + ': ' + i.get('href'))
			print()
	else:
		print('Сервер не ответил качественным конектом')

info_avinfo(url_creater_avinfo(pfone))		