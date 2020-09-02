#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# Function should return highest even number

def highest_even1(lis):
    '''
    Function returns highest even number
    '''
    
    hi_even=0
    for num in lis:
        # print (num)
        if num % 2 == 0 and num > hi_even:
            hi_even = num
    return hi_even

print(highest_even1([11,1,2,3,10,4,5,13]))


def highest_even2(lis):
    '''
    Function returns highest even number
    '''
    evens = []
    for num in lis:
        
        if num % 2 == 0:
            evens.append(num)
    return max(evens)

print(highest_even2([11,1,2,3,10,4,5,13]))

