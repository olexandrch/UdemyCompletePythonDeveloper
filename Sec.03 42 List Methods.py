#!/usr/bin/python

# Python 3
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 42. List Methods

listN1 = [1,2,3,4,5,6,7,8,9]

print(len (listN1))

# https://www.w3schools.com/python/python_ref_list.asp

# Method 	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

listN1.append(10)
listN1.pop(0)
listN1.insert(4,'5a')
print(listN1)

listN2=listN1.copy()    # copy list
listN2.pop(0)
listN2.pop()            # delete the last element
print(listN1)
print(listN2)

listN2.extend(listN1)   # add iterable items in the list
print(listN2)

print('-' * 20)
print(listN2.index('5a'))

print( 5 in listN2, 12 in listN2)
print(listN2.count('5a'))

print('*' * 20)
listN3= ["q", 'w', "a", 'r','we', 'm']         # Sort doest't work to sort INT and STR items.

print("sorded, but a new list",sorted(listN3))  # Creates a new sorted list
print("unsorded original",listN3)          # Print UNsort the list
listN3.sort()          # Sort the list
print("sorted",listN3)
listN3.reverse()       # Reverse the list
print("reversed",listN3)


# 45. Common List Patterns
print('=' * 20)
print (range(1,100))
print (list(range(1,100)))
