#Item 31 - Tips when iterating over arguments
#iterating over a list multiple time
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100

#Scale up the exercise
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

path = 'my_numbers.txt'
with open(path, 'w') as f:
    for i in (15, 35, 80):
        f.write('%d\n' % i)

it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages) #doesn't work - exhausted 

it = read_visits('my_numbers.txt')
print(list(it))
print(list(it)) #already exhausted

#solution
def normalize_copy(numbers):
    numbers_copy = list(numbers) #copy the iterator
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages_1 = normalize_copy(visits)
print(percentages_1)

it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages) #works
assert sum(percentages) == 100

#when the input is too large the previous approach can crash
#new solution
def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result

path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path)) #creates iter
print(percentages)
assert sum(percentages) == 100

#a better way to do this without the lambda (iterator protocol)
class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path
    def __iter__(self): #this way the iterators will exhaust independently
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)

#What not to do with iterators
def normalize_defensive(numbers):
    if iter(numbers) in numbers: #do not do this
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

#Alternative solution
from collections.abc import Iterator

def normalize_defensive(numbers):
    if isinstance(numbers, Iterator): #a way to check for problems
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percentage = 100 * value / total
        result.append(percentage)
    return result

visits = [15, 35, 80]
percentages_2 = normalize_defensive(visits)
assert sum(percentages_2) == 100

visits = ReadVisits(path)
percentages_3 = normalize_defensive(visits)
assert sum(percentages_3) == 100

visits = [15, 35, 80]
it = iter(visits)
normalize_defensive(it)
