import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
print(soup.body.contents)  # returns a list
print(soup.findAll('a'))
print(soup.find('span').find(id='score_30560573'))
print(soup.a)
print(soup.title)
print(soup.select('.score'))   # css selector -> grabs the entire class score.
print(soup.select('#score_30554723')) # css selector -> grabs ID. 
