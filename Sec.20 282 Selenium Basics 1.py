#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 282. Selenium Basics 1

# https://www.seleniumeasy.com/test/


# http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/

from selenium import webdriver

browser = webdriver.Firefox()

browser.maximize_window()

browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo - Simple Form to Automate using Selenium' in browser.title

showMessageButton = browser.find_element_by_class_name("btn-default")
print (showMessageButton.get_attribute('innerHTML'))

assert 'Show Message' in browser.page_source

userMessage = browser.find_element_by_id("user-message")
userMessage.clear()
userMessage.send_keys('This is my message ;-)')

showMessageButton.click()

outputUserMessage=browser.find_element_by_id("display")
print (outputUserMessage.text)
# assert 'This is my message ;-)' in outputUserMessage


browser.quit()
