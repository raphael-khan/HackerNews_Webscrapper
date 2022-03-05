import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

links = print(soup.select('.titlelink')[0])

votes = print(soup.select('.score')[0])
