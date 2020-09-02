#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 189. Exercise Regular Expressions
# Password Validation

# https://docs.python.org/3/howto/regex.html
# https://www.w3schools.com/python/python_regex.asp
# https://regex101.com/

# Password 8 letters long, letters, numbers, $%#@

import re

passwords = ('skdkjdjs', 'SsdfsdfDS$', 'dsa', '$s@ad',
             '%djfghds73535', '1234567', '12345678', '123456789', '!123456789')

for password in passwords:
    a = re.fullmatch(r'[a-zA-Z0-9$%#@]{8,}', password)
    if a:
        print(f"Password `{password}` match the criteria: {a}")
    else:
        print(f"Password `{password}` doesn't match the criteria")
