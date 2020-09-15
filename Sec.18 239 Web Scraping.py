#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 239. Web Scraping Introduction

# https://www.synerzip.com/blog/web-scraping-introduction-applications-and-best-practices/
# https://www.crummy.com/software/BeautifulSoup/
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors
# https://www.w3schools.com/css/css_selectors.asp
# https://www.w3schools.com/cssref/css_selectors.asp

# pip install beautifulsoup4
# pip install requests
from bs4 import BeautifulSoup
import requests

res = requests.get('https://news.ycombinator.com/news')

# print (res.text)

soup = BeautifulSoup(res.text, 'html.parser')

# print (soup)
# print (soup.body)
# print (soup.body.contents)
# print (soup.find_all('div'))
# print (soup.find_all('a'))
# print (soup.find('a'))
# print (soup.select('.score')) # print all sore classes: <span class="score" id="score_24483283">518 points</span>

links = soup.select('.storylink')
votes = soup.select('.score')

print (links[0], votes[0])
