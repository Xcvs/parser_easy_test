import requests
from bs4 import BeautifulSoup as bs
from random import choice, uniform
from time import sleep


headers = {'accept': '*/*', 
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}


print('Введите номер телефона:')
pfone = input()

print('Выберете регион для nomer.org:')
print('1. Москва')
print('2. Екатеренбург')
print('3. Новосибирск')
print('4. Ростов')
region = input()
region_id = int(region) - 1
print()



def url_creater_nomerorg(pfone_number):
	stable_url = 'http://nomerorg.fun/'
	pfone_url = str(pfone)
	region_catalof_list = ['mosgibdd','ektgibdd','novosibgibdd','rostovgibdd']
	base_url = stable_url + region_catalof_list[region_id] + '/phone_' + pfone + '__pagenumber_0.html'
	return base_url

def info_nomerorg(base_url):
	session = requests.Session()
	request = session.get(base_url, headers=headers)
	if request.status_code == 200:
		print('Code 200 +')
		print()
		soup = bs(request.content, 'html.parser')
		items = soup.find_all('td')
		i = int(0)
		for item in items:
			print(item.text)
			i += 1
			if i % 9:
				continue
			else:
				print()
	else:
		print('Сервер не ответил качественным конектом')



info_nomerorg(url_creater_nomerorg(pfone))		
