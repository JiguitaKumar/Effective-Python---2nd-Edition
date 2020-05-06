#Item 27 - Comprehensions vs map and filter
#a simple loop

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for x in a:
    squares.append(x**2)

print(squares)

#using map
alt = map(lambda x: x**2, a)
list(alt)

#using filter
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
list(alt)

#using a list comprehension
squares_1 = [x**2 for x in a]
squares_1

even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)
assert even_squares == list(alt)

#Dictionaries and sets 
even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
threes_cubed_set = {x**3 for x in a if x % 3 == 0}
print(even_squares_dict)
print(threes_cubed_set)

alt_dict = dict(map(lambda x: (x, x**2),
                    filter(lambda x: x % 2 == 0, a)))
alt_set = set(map(lambda x: (x, x**3),
                  filter(lambda x: x % 3 == 0, a)))
list(alt_dict)
list(alt_set)
