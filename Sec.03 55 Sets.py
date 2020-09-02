#!/usr/bin/python

# Python 3
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# https://www.w3schools.com/python/python_sets.asp
# https://www.w3schools.com/python/python_ref_set.asp


# 55. Set - unordered collection of unique object

my_set = {1,2,3,4,5,6,5,5,5,5,5,5,5,5,5,5}  # Set will have only one 5

my_set.add(99)  # Will be added
my_set.add(2)   # Will not be added

print (my_set)


# Convert list to a set (unique value only)
my_list = [1,2,3,4,5,6,5,5,5,5,5,5,5,5,5,5]
my_set2 = set(my_list)

print("my_list: ", my_list)
print("my_set2: ", my_set2)

print("5 in my_set2: ", 5 in my_set2)
print("len(my_set2): ", len(my_set2))

my_list2 = list(my_set)
print("my_list2: ", my_list2)

# Copy set
my_set3 = my_set2.copy()

# 56. Set2. Methods

