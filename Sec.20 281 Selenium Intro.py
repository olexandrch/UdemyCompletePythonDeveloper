#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 281. Selenium Introduction

# https://selenium-python.readthedocs.io/

# Install Selenium
# $ pip install selenium

# Install Drivers for browser
# Firefox: 	https://github.com/mozilla/geckodriver/releases
# https://pypi.org/project/selenium/


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

# browser.quit()
