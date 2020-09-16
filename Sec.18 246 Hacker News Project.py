#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 246. Hacker News Project

# https://www.synerzip.com/blog/web-scraping-introduction-applications-and-best-practices/
# https://www.crummy.com/software/BeautifulSoup/
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# https://scrapy.org/

# https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors
# https://www.w3schools.com/css/css_selectors.asp
# https://www.w3schools.com/cssref/css_selectors.asp

# https://docs.python.org/3/library/pprint.html


# pip install beautifulsoup4
# pip install requests
from bs4 import BeautifulSoup
import requests
import pprint

RES= 'https://news.ycombinator.com/news'
POINTS = 200

res = requests.get(RES)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

for i in range(2,4):
    res = requests.get(RES+'?p='+str(i))
    soup = BeautifulSoup(res.text, 'html.parser')
    links += soup.select('.storylink')
    subtext += soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['points'], reverse=True)
    
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title= item.getText()
        href=item.get('href', None)
        vote=subtext[idx].select('.score')
        if len(vote):
            points=int(vote[0].getText().replace(' points', ''))
            if points >= POINTS:
                hn.append({'title':title, 'link':href, 'points':points})
    return sort_stories_by_votes(hn)


hacker_news= create_custom_hn(links, subtext)
pprint.pprint(hacker_news)

