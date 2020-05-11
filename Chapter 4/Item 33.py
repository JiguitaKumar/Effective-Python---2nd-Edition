#Item 33 - composing multiple generators
#the noisy approach
def move(period, speed):
    for _ in range(period):
        yield speed

def pause(delay):
    for _ in range(delay):
        yield 0

def animate():
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta

def render(delta):
    print(f'Delta: {delta:.1f}')
    # Move the images onscreen

def run(func):
    for delta in func():
        render(delta)

run(animate)

#the solution (yield from)
def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)

run(animate_composed)

#verifying the speedup of the solution
import timeit

def child():
    for i in range(1_000_000):
        yield i

def slow():
    for i in child():
        yield i

def fast():
    yield from child()

baseline = timeit.timeit(
    stmt = 'for _ in slow(): pass',
    globals = globals(),
    number = 50)
print(f'Manual nesting {baseline:.2f}s')

comparison = timeit.timeit(
    stmt = 'for _ in fast(): pass',
    globals = globals(),
    number = 50)
print(f'Composed nesting {comparison:.2f}s')

reduction = - (comparison - baseline) / baseline
print(f'{reduction:.1%} less time')