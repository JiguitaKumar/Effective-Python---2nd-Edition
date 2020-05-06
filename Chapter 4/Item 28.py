#Item 28 - Avoid more then 2 control subexpressions in comprehensions
#using 2 "for" subexpressions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)
matrix

#test
flat1 = [x for x in matrix]
flat1

squared = [[x**2 for x in row] for row in matrix]
print(squared)

#test
squared2 = [x**2 for row in matrix for x in row]
print(squared2)

#more than 2 subexpressions (too long)
my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
]

flat2 = [x for sublist1 in my_lists
         for sublist2 in sublist1
         for x in sublist2]
flat2

"""Note:The number "levels" of pair of squared brackets matches the \
    number of subexpressions that you need
"""

#test
c1 = [x for x in my_lists]
c1

c2 = [x for y in my_lists for x in y]
c2

c3 = [x for y in my_lists for z in y for x in z]
c3

#normal loop (not much different from comprehension)
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)

flat

#Multiple if conditions
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e = [x for x in d if x % 2 == 0 if x > 4]
f = [x for x in d if x % 2 == 0 and x > 4]
e
f

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
filtered