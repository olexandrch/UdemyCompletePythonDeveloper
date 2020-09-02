#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 184. Exercise: Translator

# Lets build a translator in python
# https://github.com/terryyin/translate-python

# need to install the translate module first
# $ pip install translate

from translate import Translator

translator = Translator(to_lang="ru")


try:
    with open('Sec.13 180 Working With Files In Python.txt', mode='r') as my_file:
        text_to_translate = (my_file.read())
except FileNotFoundError as err:
    print('File doesn\'t exist. Error = ', err)
finally:
    print('All done')

text_translated = translator.translate(text_to_translate)

print(text_translated)
