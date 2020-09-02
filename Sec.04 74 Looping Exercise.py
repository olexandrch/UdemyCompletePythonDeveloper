#!/usr/bin/python

# Python 3
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 74. Our First GUI

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


fill =  '+'
empty = ' '
for line in picture:
    for pixel in line:
        if pixel:       # We can do (pixel == 1) but we know it is the same
            print(fill, end ='')
        else:
            print(empty, end ='')
    print()


# a, b = 2,4
# print (f'a = {a} and b = {b}')
