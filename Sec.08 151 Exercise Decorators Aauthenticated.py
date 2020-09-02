#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 151. Decorators
# https://www.programiz.com/python-programming/decorator

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrap_func(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrap_func


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
