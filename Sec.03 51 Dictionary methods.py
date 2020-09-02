#!/usr/bin/python

# Python 3
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/


dic2 = {
    'a':[1,2,3,4,5],
    22:"Hello There",
    'bb':True
}

# 51. Dictionary methods

# https://www.w3schools.com/python/python_ref_dictionary.asp

print ("dic2.get('a'): ", dic2.get('a'))
print ("dic2.get('Absent_Key'): ", dic2.get('Absent_Key'))
# Add default value
print ("dic2.get('Absent_Key', 999): ", dic2.get('Absent_Key', 999))

# Another method to create dictionary. Not a very common way to create a dictionary
dic3 = dict(name='Alex', age=33)
print ("dic3: ", dic3)

# 52. Dictionary methods 2

print ("'age' in dic3: ", 'age' in dic3)
print ("'Age' in dic3: ", 'Age' in dic3)
print ("'size' in dic3: ", 'size' in dic3)

print ("'age' in dic3.keys(): ", 'age' in dic3.keys())
print ("33    in dic3.values(): ", 33 in dic3.values())

print ("dic3.items(): ", dic3.items())

# Copy and clear dictionary
dic3_copy = dic3.copy()
dic3.clear()

print ("dic3_copy: ", dic3_copy)
print ("dic3: ", dic3)

# Remove a key-value pair
print("dic3_copy.pop('age'): ", dic3_copy.pop('age'))
print("dic3_copy: ", dic3_copy)

# Update / ADD items
dic3_copy.update({'name':'Johnny Depp'})
dic3_copy.update({'Age':99})
print("dic3_copy:  ", dic3_copy)
