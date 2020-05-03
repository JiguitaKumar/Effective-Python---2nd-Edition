# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:53:26 2020

@author: jiguitakumar
"""

#Item 22 - Variable positional arguments (varargs / star args)
def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

log('My numbers are', [1, 2])
log('Hi there', [])

#avoiding empty lists
def log(message, *values): #means that the 2nd variable is optional
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')
    
log('My numbers are', 1, 2)
log('My numbers are', *[1, 2])
log('Hi there')

favorites = [7, 33, 99]
log('favorite colors', *favorites)

#problems with variable positional arguments
def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it) # memory consumming


def log(sequence, message, *values):
    if not values:
        print(f'{sequence} - {message}')
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{sequence} - {message}: {values_str}')

log(1, 'Favorites', 7, 33)
log(1, 'Hi there')
log('Favorite numbers', 7, 33) #where the problem is