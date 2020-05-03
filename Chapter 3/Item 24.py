#Item 24 - Using None and docstrings
#Non-static keyword arguments
from time import sleep
from datetime import datetime

def log(message, when=datetime.now()):
    print(f'{when}: {message}')
    
log('Hi there')
sleep(0.1)
log('Hello there') #doesn't work as expected

#solution (provide a default value None)
def log1(message, when = None):
    """Log a message with a timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occured.
            Defaults to the present time
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

log1('Hi there!')
sleep(0.1)
log1('Hello again!')

#test
def log2(message, when=None):
    print(f'{when}: {message}')

log2('Hello world', datetime.now())

#using None is specially important when the argument is mutable

#additional example
import json

def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('Bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar) #not good

assert foo is bar
assert foo == bar

#solving
def decode1(data, default = None):
    """Load JSON data from a string.
    
    Args:
        data: JSON data to decode
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default

foo = decode1('bad data')
foo['stuff'] = 5
bar = decode1('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
assert foo is not bar

#using typing
from typing import Optional

def log_typed(message: str,
              when: Optional[datetime]=None) -> None:
    """Log a message with a timestamp.
    
    Args:
        message: Message to print.
        when: datetime of when the message occured.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

log_typed('hi there')