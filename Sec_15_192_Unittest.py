#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 192. Unittest

def do_stuff(num=0):
    try:
        if (num != None) and (num != ''):
            return int(num)+5
        else:
            return "Please enter number"

    except ValueError as err:
        return err
