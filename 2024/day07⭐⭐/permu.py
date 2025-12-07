from itertools import permutations

operator = ['+', 'x', '|']

print([p for p in list(permutations(operator, 3))])