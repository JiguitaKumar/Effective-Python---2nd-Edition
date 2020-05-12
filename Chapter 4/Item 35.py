#Item 35 - State Transitions in generators
#using the Throw method
class MyError(Exception):
    pass

def my_generator():
    yield 1
    yield 2
    yield 3

it = my_generator()
print(next(it))
print(next(it))
print(it.throw(MyError('test error')))

#using try and except
def my_generator():
    yield 1
    
    try:
        yield 2
    except MyError:
        print('Got MyError!')
    else:
        yield 3
    
    yield 4

it = my_generator()
print(next(it))
print(next(it))
print(it.throw(MyError('test error')))

#a practical case in which this is useful
class Reset(Exception):
    pass

def timer(period):
    current = period
    while current:
        current -=1
        try:
            yield current
        except Reset:
            current = period

RESETS = [
    False, False, False, True, False, True, False,
    False, False, False, False, False, False, False]

def check_for_reset():
    #Poll for exerternal event
    return RESETS.pop(0)

def announce(remaining):
    print(f'{remaining} ticks remaining')

def run():
    it = timer(4)
    while True: #means loop forever
        try:
            if check_for_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)

run()

#simpler approach to achieve the same result
class Timer:
    def __init__(self, period):
        self.current = period
        self.period = period
    
    def reset(self):
        self.current = self.period
    
    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current

RESETS = [
    False, False, False, True, False, True, False,
    False, False, False, False, False, False, False]

def check_for_reset():
    #Poll for exerternal event
    return RESETS.pop(0)

def run():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        announce(current)

run()

"""Avoid using throw entirely if you need this type of exceptional
    behavior
"""