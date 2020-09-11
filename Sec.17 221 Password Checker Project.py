#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 221. Password Checker Project

# https://haveibeenpwned.com/Passwords
# https://pypi.org/project/requests/
# https://passwordsgenerator.net/sha1-hash-generator/

import requests
import hashlib

# password123 - SHA1 - CBFDAC6008F9CAB4083784CBD1874F76618D2A97
# API accept 5 first symbols from SHA1

def request_api_data(query_char):
    """Provides API with the first 5 symbols of SHA1 hash of the passoword and get response if it was pwned"""
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def pwned_api_check(password):
    """Check Password if it exists in API response"""
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password


print(request_api_data('CBFDA'))
print(pwned_api_check('password123'))