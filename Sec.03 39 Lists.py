#!/usr/bin/python

# Python 3
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 39. Lists
# Similar to arrays in other languages

listN1=[1,2,3,4,5,6,7]
listN2=['a','b','c','d', 'e', 'f']
listN3=[
    1,
    2,
    3.333,
    4.444, 5.5555, '6a', '7b','8c','d',True, False]

print (listN1,listN2, listN3)

for item in listN3:
    print (f"Item is {item} and type is {type(item)}")

# 40. List slicing

print (listN3[-3],listN3[1:7:2], listN3[::-1])

# Lists are mutable
listN1[1]=99
print (listN1)

# When you assing a new list an old list, it is just point to the old list.
# It doesn't copy all elements in the list.
print ('-'*20)
listN1new=listN1
listN1new[1]=111
print (listN1)  # it changes a new list and the old list
print (listN1new)

# If we want to copy list do with the slices
print ('*'*20)
listN1newNew=listN1[:]   # it copy all elements of the list now
listN1newNew[1]=999
print (listN1)
print (listN1newNew)    # it changes only newNew list



