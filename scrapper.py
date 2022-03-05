import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
print(soup.body.contents)  # returns a list
print(soup.findAll('a'))
print(soup.find(id='score_30560573'))
print(soup.a)
print(soup.title)

