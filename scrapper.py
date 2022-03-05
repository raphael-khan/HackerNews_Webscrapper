import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

links = soup.select('.titlelink')

subtext = soup.select('.subtext')

def sort_stories_by_votes(news): 
    return sorted(news, key=lambda k:k['votes'] , reverse=True)  # sorting a dictionary by votes in increasing order. 

## Function that gets us the title, links and score of every post on the newsfeed ##
def create_custom_news(links, subtext):
    news = []
    for  idx, item in enumerate(links):
        title = links[idx].getText()         # gets us the text or title in this case. 
        href = links[idx].get('href', None)   # None in case if a post does not have a link. 
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                news.append({'title': title, 'link': href, 'votes': points})    # appends a dictionary  to the list since we have more than one variable. 
    return sort_stories_by_votes(news)

pprint.pprint(create_custom_news(links, subtext))