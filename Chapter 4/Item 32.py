#Item 32 - Generators for large list comprehensions 
#The problem with list comprehensions
import random

with open('my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

value = [len(x) for x in open('my_file.txt')]
print(value)

#when the input is large, the generators are more appropriate
it = (len(x) for x in open('my_file.txt'))
print(next(it))
print(next(it))

#generators composed together
roots = ((x, x**0.5) for x in it)
print(next(roots))
