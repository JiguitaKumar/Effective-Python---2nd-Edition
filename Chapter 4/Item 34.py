#Item 34 - Using send in generators
#having a bidirectional communication (stream data in and out as it runs)
import math

def wave(amplitude, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output

def transmit(output):
    if output is None:
        print(f'Output is None')
    else:
        print(f'Output: {output:>5.1f}')

def run(it):
    for output in it:
        transmit(output)

run(wave(3.0, 8))

#moduling the amplitude to change at each interaction
#using next
def my_generator():
    received = yield 1
    print(f'received = {received}')

it = iter(my_generator())
output = next(it)
print(f'output = {output}')

try:
    next(it)
except StopIteration:
    pass

it = iter(my_generator())
output = it.send(None)
print(f'output = {output}')

try:
    it.send('hello!')
except StopIteration:
    pass

#using send
def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield #input yield (received through send())
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output #output yield

def run_modulating(it):
    amplitudes = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)

run_modulating(wave_modulating(12))

#complicating a little more (multiple signals in sequence)
def complex_wave():
    yield from wave(7.0, 3)
    yield from wave(2.0, 4)
    yield from wave(10.0, 5)

run(complex_wave())


def complex_wave_modulating():
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)

run_modulating(complex_wave_modulating())
"""conclusion: the yield from and send features behave individually,
    they will break if you try to use them together
    avoid using send()
"""

#Alternative approach
def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step_size * step
        fraction = math.sin(radians)
        amplitude = next(amplitude_it) #gets next input
        output = fraction * amplitude
        yield output

def complex_wave_cascading(amplitude_it):
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 4)
    yield from wave_cascading(amplitude_it, 5)

def run_cascading():
    amplitudes = [7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    it = complex_wave_cascading(iter(amplitudes))
    for amplitude in amplitudes:
        output = next(it)
        transmit(output)

run_cascading()