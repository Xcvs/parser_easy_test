import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*', 
	    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4056.3 Safari/537.36'}

base_url = 'https://www.srosa.ru/voda/produktsija'

def user_cread(base_url, headers):
	session = requests.Session()
	request = session.get(base_url, headers=headers)
	if request.status_code == 200:
		print('Code 2007')
		soup = bs(request.content, 'html.parser')
		pages = soup.find('div', attrs = {'class': 'blog-record-description'})
		contents = pages.text
		contents = content.split('.')
                return contents
        else:
		print('Error')

user_cread(base_url, headers)	    
