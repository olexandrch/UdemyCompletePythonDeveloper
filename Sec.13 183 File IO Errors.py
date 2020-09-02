#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 183. File IO Errors
# https://www.idkrtm.com/error-handling-in-python-using-with-and-try/

try:
    with open('Sec.13 180 Working With Files In Python.txt', mode='r') as my_file:
        print(my_file.readlines())
except FileNotFoundError as err:
    print('File doesn\'t exist. Error = ', err)
finally:
    print('All done')


try:
    with open('NotExistingFile.txt', mode='r') as my_file:
        print(my_file.readlines())
except FileNotFoundError as err:
    print('File doesn\'t exist.\nError = ', err)
finally:
    print('All done')
