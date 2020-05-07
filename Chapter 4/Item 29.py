#Item 29 - Assignment expressions in comprehensions
#repetition issue
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']

def get_batches(count, size):
    return count // size

result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches

print(result)

#same logic using dict comprehension
found = {name: get_batches(stock.get(name, 0), 8)
         for name in order
         if get_batches(stock.get(name, 0), 8)} #repeats code
found

has_bug = {name: get_batches(stock.get(name, 0), 4)
           for name in order
           if get_batches(stock.get(name, 0), 8)}

print(f'Expected:', found)
print('Found:   ', has_bug)

#solution
found = {names: batches 
         for name in order
         if (batches := get_batches(stock.get(name, 0), 8))}

result = {name: (tenth := count // 10) #wrong
          for name, count in stock.items()
          if tenth > 0}

result = {name: tenth
          for name, count in stock.items()
          if (tenth := count // 10) > 0} #solved
print(result)

#using walrus in the value part
half = [(last := count // 2) for count in stock.values()] #leaks loop
print(f'Last item of {half} is {last}')

for count in stock.values(): #also leaks
    pass
print(f'Last item of {list(stock.values())} is {count}')

half = [count // 2 for count in stock.values()]
print(half) 
print(count) #didn't leak

"""Conclusion: it is recommended to use assignment expressions \
    only in the condition part of the comprehension
"""

#in generating expressions
found = ((name, batches) for name in order
         if (batches := get_batches(stock.get(name, 0), 8)))
print(next(found))
print(next(found))