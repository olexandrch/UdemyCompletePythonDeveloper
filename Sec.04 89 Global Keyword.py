#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 89. Scope. Global Keyword


total = 0

def count():
    '''
    Function to demonstrate global keyword
    '''
    global total
    total += 1

    return total
    
count()
count()
count()
print(count())
