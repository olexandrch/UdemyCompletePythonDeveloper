#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 181. Read, Write, Append
# with statement in Python
# https://www.geeksforgeeks.org/with-statement-in-python/

# You don't need to close the file while using with statement

# mode='r' to read file
# mode='w' to write file
# mode='a' to append file
# mode='r+' to read/write file
with open('Sec.13 180 Working With Files In Python.txt', mode='r') as my_file:
    print(my_file.readlines())

# mode='r+' to read and write the file
with open('Sec.13 180 Working With Files In Python.txt', mode='r+') as my_file:
    file_lines = my_file.readlines()
    my_file.write(':-)')
