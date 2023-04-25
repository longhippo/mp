import requests
from bs4 import BeautifulSoup

url = 'https://github.com/scrapy/scrapy/graphs/contributors'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
contributors = soup.find_all('div', class_='contrib-person')

for contributor in contributors:
    username = contributor.find('a').find('span').get_text()
    contributions = contributor.find('span', class_='contrib-number').get_text()
    print(f'Username: {username}, Contributions: {contributions}')
