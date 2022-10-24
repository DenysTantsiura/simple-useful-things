from itertools import product, permutations

letters = ("A", "B", "C")
print(list(product(letters, range(2))))
print()
print(list(permutations(letters)))

"""
[('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]

[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

"""