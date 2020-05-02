# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:38:00 2020

@author: jiguitakumar
"""

#Item 20 - Raise exception vs Returning None
#when using none makes sense
def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print('Invalid inputs')

x, y = 0, 5
result = careful_divide(x, y)
if not result:
    print('Invalid inputs') #it is a false-equivalent

#other ways to reduce the change of error (Split into 2-tuple)
def careful_divide(a, b):
    try:
        return True, a/b
    except ZeroDivisionError:
        return False, None

success, result = careful_divide(x, y)
if not success:
    print('Invalid inputs')

_, result = careful_divide(x, y)
if not result:
    print('Invalid inputs')
    
# second better way (Raise exception)
def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')
        
x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result if %.1f' % result)

#what the correct function should look like with annotations
def careful_divide(a: float, b: float) -> float:
    """Divides a by b.
    
    Raises:
        ValueError: When inputs cannot be divided.
    """
    
    try:
        return a / b
    except ValueError:
        raise print('Invalid inputs')