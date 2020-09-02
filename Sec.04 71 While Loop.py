#!/usr/bin/python

# Python 3
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 71. While Loop
# https://www.w3schools.com/python/python_while_loops.asp

a, b = 2,4
print (f'a = {a} and b = {b}')


i = 0
while i < 99:
  i += 1
  if i == 2 or i == 4:
    print(" ", end =" ")
    continue
  print(i, end =" ")
  if i == 7:
    break
print()

i = 0
while i < 6:
  i += 1
  print(f'i = {i}')

else:
    print (f"this is the end of the else loop. Executing else: . i = {i}")
print()


while True:
    text= input('say something. Enter for exit:  ')
    if text == '':
        break
    print (f'you just said: {text}')
    
