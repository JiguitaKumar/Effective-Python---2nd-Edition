#Item 38 - Functions vs Classes in APIs
#sorting a list with key argument
name = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
name.sort(key=len)
print(name)

#handling missing values
def log_missing():
    print('key added')
    return 0

from collections import defaultdict

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

result = defaultdict(log_missing, current)
print('Before:', dict(result))
for key, amount in increments:
    result[key] += amount
print('After:', dict(result))

current['white'] = 3
result['black'] = 7

current.keys()
current.values()

#using log_missing
def increment_with_report(current, increments):
    added_count = 0
    
    def missing():
        nonlocal added_count #Stateful closure
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2

#simpler approach to do the same
class CountMissing:
    def __init__(self):
        self.added = 0
    
    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
result = defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2

#however the usage of the class on its own is a mistery. To solve that:
class BetterCountMissing:
    def __init__(self):
        self.added = 0
    
    def __call__(self): #now it can be called as a function
        self.added += 1
        return 0

counter = BetterCountMissing()
assert counter() == 0
assert callable(counter)

counter = BetterCountMissing()
result = defaultdict(counter, current) #relies on __call__
for key, amount in increments:
    result[key] += amount
assert counter.added == 2