#Item 36 - Using itertools
import itertools

#linking iterators together
## Chain - joins lists
it = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(it))

## Repeat - repeats the same item 3 times in the same list
it = itertools.repeat('hello', 3)
print(list(it))

## cycle - repeats the items infite times
it = itertools.cycle([1, 2])
result = [next(it) for _ in range(10)]
print(result)

## tee - assigns the same list to 3 different variables
it1, it2, it3 = itertools.tee(['first', 'second'], 3)
print(list(it1))
print(list(it2))
print(list(it3))

## zip_longest - returns a placeholder when the iterator is exhausted
keys = ['one', 'two', 'three']
values = [1, 2]

normal = list(zip(keys, values))
print('zip:        ', normal)

it = itertools.zip_longest(keys, values, fillvalue = 'nope')
longest = list(it)
print('zip_longest:', longest)

#Filtering items from an iterator
## islice - slice by numerical indexes without copying
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_five = itertools.islice(values, 5)
print('First five: ', list(first_five))

middle_odds = itertools.islice(values, 2, 8, 2)
print('Middle odds:', list(middle_odds))

## takewhile - returns items from an iterator until a function returns False
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.takewhile(less_than_seven, values)
print(list(it))

## dropwhile - skips items from an iterator until a function returns True
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.dropwhile(less_than_seven, values)
print(list(it))

## filterfalse - returns all items which are False
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = lambda x: x % 2 == 0

filter_result = filter(evens, values)
print('Filter:      ', list(filter_result))

filter_false_result = itertools.filterfalse(evens, values)
print('Filter false:', list(filter_false_result))

#Producing combinations of Items from iterators
## accumulate - folds an item from the iterator into a running value
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_reduce = itertools.accumulate(values)
print('sum:   ', list(sum_reduce))

def sum_modulo_20(first, second):
    output = first + second
    return output % 20

modulo_reduce = itertools.accumulate(values, sum_modulo_20)
print('Modulo:', list(modulo_reduce))

## product - returns the Cartesian product of items
single = itertools.product([1, 2], repeat=2)
print('Single:  ', list(single))

multiple = itertools.product([1, 2], ['a', 'b'])
print('Multiple:', list(multiple))

## permutations - returns the unique ordered permutations
#accepts both (1, 2) and (2, 1) in the same output
it = itertools.permutations([1, 2, 3, 4], 2)
print(list(it))

it = itertools.permutations([1, 2, 3, 4], 3)
print(list(it))

## combinations - returns the unique sorted combinations
#does not accept both (1, 2) and (2, 1) in the same output
it = itertools.combinations([1, 2, 3, 4], 2)
print(list(it))

it = itertools.combinations([1, 2, 3, 4], 3)
print(list(it))

## combinations with replacement - repeated values are allowed
#does not accept both (1, 2) and (2, 1) in the same output
it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
print(list(it))