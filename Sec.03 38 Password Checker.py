#!/usr/bin/python

# Python 3
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 38. Exercise: Password Checker

name=input("Input name: ")
password=input("Input password: ")

passwordLength=len(password)
starPass='*' * passwordLength


print(f'Hi {name} password {starPass} is {passwordLength} letter long')
