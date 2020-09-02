#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# Sec.10 162. Fibonacci Numbers. # Exercise.py

Fib = 10


def fibonacci1(num):
    f0 = 0
    f1 = 1

    print("Fib Number = 0 Fib = 0")
    print("Fib Number = 1 Fib = 1")
    for i in range(2, num+1):
        f2 = f0+f1
        print("Fib Number = ", i, "f2 = ", f2)
        f0 = f1
        f1 = f2


fibonacci1(Fib)


def fibonacci2(num):
    fib = [0, 1]
    for i in range(2, num+1):
        fib.append(fib[i-2]+fib[i-1])
    print("Fib Numbers = ", fib)


fibonacci2(Fib)


def fibonacci3(num):
    a = 0
    b = 1
    for i in range(num+1):
        yield a
        temp = a
        a = b
        b = temp+b


for x in fibonacci3(Fib):
    print(x)
