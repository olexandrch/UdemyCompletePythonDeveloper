#!/usr/bin/python

# Python 3
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# https://www.w3schools.com/python/python_sets.asp
# https://www.w3schools.com/python/python_ref_set.asp


# 55. Set - unordered collection of unique object
# 56. Set2. Methods

my_set1 = {1,2,3,4,5,6,5}
my_set2 = {1,2,5,11,12,13,14,15}

print (my_set1)
print (my_set2)

# .difference
print("my_set1.difference(my_set2): ", my_set1.difference(my_set2))
print("my_set2.difference(my_set1): ", my_set2.difference(my_set1))

# .discard
my_set2.discard(14)
print("my_set2 #(after discard 14)#: ", my_set2)

# .intersection  Can do with & 
print("my_set2.intersection(my_set1): ", my_set2.intersection(my_set1))
print("my_set2 & my_set1:             ", my_set2 & my_set1)

# .union Return united set. Can do with | 
print("my_set2.union(my_set1): ", my_set2.union(my_set1))
print("my_set1 | my_set2:      ", my_set1 | my_set2)
print("my_set1, my_set2: ",  my_set1, my_set2)

# .difference_update
my_set2.difference_update(my_set1)
print("my_set2 #(after my_set2.difference_update(my_set1))#: ", my_set2)

# .isdisjoint()  # It is TRUE after .difference_update
print("my_set1, my_set2:                  ",  my_set1, my_set2)
print("my_set2.isdisjoint(my_set1):       ", my_set2.isdisjoint(my_set1))

# .issubset and .issuperset
my_set3 = {1,2,3}
my_set4 = {1,2,3,4,5,6}

print("my_set3, my_set4:            ",  my_set3, my_set4)
print("my_set3.issubset(my_set4):   ", my_set3.issubset(my_set4))
print("my_set3.issuperset(my_set4): ", my_set4.issuperset(my_set3))
