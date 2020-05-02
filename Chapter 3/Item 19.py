# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:07:57 2020

@author: jiguitakumar
"""

#Item 19
#multiple return function
def get_stats(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return minimum, maximum

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

minimum, maximum = get_stats(lengths)
print(f'Min: {minimum}, Max: {maximum}')

#unpacking statement
first, second = 1, 2
assert first == 1
assert second == 2

def my_function():
    return 3, 4

third, fourth = my_function()
assert third == 3 
assert fourth == 4

#starred expressions
def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse = True)
    return scaled

longest, *middle, shortest = get_avg_ratio(lengths)
print(f'Longest: {longest:>5.0%}') #spacing of 5 and % format
print(f'Shortest: {shortest:.0%}') #in % format

#How confusing it gets with more than 3 variables
def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count
    
    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0: #quando é divisivel por 2 não tem 1 ponto médio
        lower = sorted_numbers[middle-1] #porque começa a contar do 0
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2 # a média dos 2 pontos médios
    else:
        median = sorted_numbers[middle] #quando não é divisivel por 2
    return minimum, maximum, average, median, count

minimum, maximum, average, median, count = get_stats(lengths)

print(f'Min: {minimum}, Max: {maximum}')
print(f'Average: {average}, Median: {median}, Count: {count}')
