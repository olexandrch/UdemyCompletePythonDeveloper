#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 221. Password Checker Project

# https://haveibeenpwned.com/Passwords
# https://pypi.org/project/requests/
# https://passwordsgenerator.net/sha1-hash-generator/

import requests

# password123 - SHA1 - CBFDAC6008F9CAB4083784CBD1874F76618D2A97
# API accept 5 first symbols from SHA1

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)

print (res)

