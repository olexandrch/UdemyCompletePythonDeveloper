#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 180. Working With Files In Python
# https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3
# https://www.tutorialspoint.com/python3/python_files_io.htm


my_file = open('Sec.13 180 Working With Files In Python.txt')

print()
print('='*24)
print(my_file)
print('print(my_file.read())', '='*24)
print(my_file.read())
print(my_file.read())
print(my_file.read())

# File was read only the first time.

'''
alex:$
========================
<_io.TextIOWrapper name='Sec.13 180 Working With Files In Python.txt'
mode='r'
encoding='UTF-8'>
========================
Hi there !!!
How are you doing?
[~/Dropbox/College/2020.07 Udemy Python]
'''

# We can add .seek() method to move the cursor

print('print(my_file.read())', '='*24)
my_file.seek(0)
print(my_file.read())

# .readline() method is reading only 1 line at a time

print('print(my_file.readline())', '='*24)
my_file.seek(0)
print(my_file.readline())

# .readlines() method is reading all the lines and return a list

print('print(my_file.readlines())', '='*24)
my_file.seek(0)
print(my_file.readlines())

# Close the file after using
my_file.close()
