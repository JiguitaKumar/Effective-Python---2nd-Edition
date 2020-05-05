#Item 26 - Decorators (functools.wrap)
"""Decorators have the ability to run additional code before and \
    after each call to a function it wraps.

Remainder: *args - the argument is optional
           **Kwargs - adopts any arguments
"""

#decorator
def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r})'
              f' -> {result!r}')
        return result
    return wrapper

#applying the decorator using @
#@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))

fibonacci = trace(fibonacci)
fibonacci(4)

#test
def tentativa(func):
    def teste():
        print('Hello')
        func()
        print('Bye')
    return teste

def tentativa2():
    print('attempt')
    
tentativa2 = tentativa(tentativa2)
tentativa2()

#test2
@trace
def fibonacci_2(n):
    if n in (0,1):
        return n
    return (fibonacci_2(n-2) + fibonacci_2(n-1))

fibonacci_2(4)

print(fibonacci) #the problem. It doesn't assume the name
help(fibonacci)

#solution - use the functools - wraps helper function
import pickle

pickle.dumps(fibonacci)

from functools import wraps

def trace2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r})'
              f' -> {result!r}')
        return result
    return wrapper

@trace2
def fibonacci_3(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci_3(n - 2) + fibonacci_3(n - 1))

help(fibonacci_3)

print(pickle.dumps(fibonacci_3))