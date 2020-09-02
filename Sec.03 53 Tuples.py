#!/usr/bin/python

# Python 3
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# https://www.w3schools.com/python/python_tuples.asp
# https://www.w3schools.com/python/python_ref_tuple.asp


# 53. Tuple - immutable list

my_tuple = (1,2,3,4,5,6)

#     my_tuple[1] = 99   Will not work. Error.
print(my_tuple[1])

print(5 in my_tuple)

# We can use tuples as a key in a dictionary, because they are immutable.
dic2 = {
    (11,22):[1,2,3,4,5],
    22:"Hello There",
    'bb':True
}

print("dic2[(11,22)]: ", dic2[(11,22)])

# Slices of tuple
new_tuple = my_tuple[1:4]
print (new_tuple)

# Assignments
x,y,z, *other = (1,2,3,4,5,6,55,7,55,8,55,9)

print ("x: ", x)
print ("y: ", y)
print ("z: ", z)
print ("other: ", other)

# Count and index methods
my_tuple2 = (1,2,3,4,5,6,55,7,55,8,55,9)
print ("my_tuple2.count(55): ", my_tuple2.count(55))
print ("my_tuple2.index(55): ", my_tuple2.index(55))

print ("len(my_tuple2): ", len(my_tuple2))
