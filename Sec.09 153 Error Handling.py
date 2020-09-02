#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 153. Error Handling
# https://www.w3schools.com/python/gloss_python_error_handling.asp
# https://wiki.python.org/moin/HandlingExceptions
# https://docs.python.org/3/library/exceptions.html


while True:
    try:
        age = int(input('153. what is your age?: '))
        print('10/age is: ', 10/age)
    except ValueError:
        print("Age should be a number")
    except ZeroDivisionError:
        print("Age should not be 0")
    else:
        print('Thank you!')
        break


# 154. Error Handling2

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'please enter 2 numbers. We got the error: <<{err}>>')


print(sum(4, '2'))


def divis(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'please enter 2 numbers. We got the error: <<{err}>>')


print(divis(33, 3))
print(divis(4, 0))
print(divis(4, '5'))

# 155. Exercise

while True:
    try:
        age = int(input('155. what is your age?: '))
        print('10/age is: ', 10/age)
    except ValueError:
        print("Age should be a number")
    except ZeroDivisionError:
        print("Age should not be 0")
    else:
        print('Thank you!')
        break
    finally:
        print('OK, this section will run no matter what')

# 156. Error Handling3

while True:
    try:
        age = int(input('156. what is your age? Input number: '))
        print('10/age is: ', 10/age)
        raise Exception('Heyyyy, Cut it out!!!!')
    except ValueError:
        print("Age should be a number")
    except ZeroDivisionError:
        print("Age should not be 0")
    else:
        print('Thank you!')
        break
    finally:
        print('OK, this section will run no matter what')
