from pathlib import Path
from math import sqrt
import numpy as np
from scipy.optimize import linprog

example = True # False # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

# tasks = []
# for l in open(file).read().split('\n'):
#     toggles, *buttons, counters = l.split()
#     toggles = [x == "#" for x in toggles[1:-1]]
#     moves = [set(map(int, b[1:-1].split(","))) for b in buttons]
#     counters = list(map(int, counters[1:-1].split(",")))
#     tasks.append((toggles, moves, counters))

# def solve(goal, moves, part1):
#     n, m = len(moves), len(goal)
#     c = [1] * n
#     A_eq = [[i in move for move in moves] for i in range(m)]
#     bounds = [(0, None)] * n
#     if part1:
#         c += [0] * m
#         A_eq = np.hstack([A_eq, -2 * np.eye(m)])
#         bounds += [(None, None)] * m
#     return linprog(c, A_eq=A_eq, b_eq=goal, bounds=bounds, integrality=True).fun

# # Part 1
# print(sum(solve(goal, moves, True ) for goal, moves, _ in tasks))
# # Part 2
# print(sum(solve(goal, moves, False) for _, moves, goal in tasks))

from itertools import combinations

a = b = 0
for diagram, *buttons, joltage in map(str.split, open(file)):
    diagram = [c=='#' for c in diagram[1:-1]]
    buttons = [eval(b[:-1]+',)') for b in buttons]
    joltage = eval(joltage[1:-1])
    numbers = range(len(joltage))

    def toggle(buttons):
        for n in numbers:
            for pressed in combinations(buttons, n):
                lights = [sum(i in p for p in pressed)%2 for i in numbers]
                if lights == diagram: return n

    a += toggle(buttons)

    c = [1 for _ in buttons]
    A = [[i in b for b in buttons] for i in numbers]

    b += linprog(c, A_eq=A, b_eq=joltage, integrality=1).fun

print(a, int(b))