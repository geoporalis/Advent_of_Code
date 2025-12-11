from pathlib import Path
from math import sqrt
import numpy as np
import scipy
# from scipy.optimize import linprog

example = False # True # 

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

    b += scipy.optimize.linprog(c, A_eq=A, b_eq=joltage, integrality=1).fun

print(a, int(b))

# import time
# import re

# with open(file, 'r') as f:
#     inp = f.read()

# inp = inp.split('\n')
# if len(inp[-1]) == 0:
#     inp.pop()

# machines = []
# buttons = []
# joltages = []

# for line in inp:
#     mach = re.findall(r'\[([^\]]*)\]', line)
#     machines.append(mach[0])

#     buts = re.findall(r'\(([^\(]*)\)', line)
#     buts = [[int(x) for x in but.split(',')] for but in buts]
#     buttons.append(buts)

#     jolts = re.findall(r'\{([^\{]*)\}', line)
#     jolts = [int(x) for x in jolts[0].split(',')]
#     joltages.append(jolts)



# def find_xors(target, nums):
#     ans = []
#     n = len(nums)
#     least = n + 1

#     for i in range(2**n):
#         # Each i is one subset
#         xor = 0
#         subset = []
#         for j in range(n):
#             if (i >> j) % 2 == 1:
#                 xor ^= nums[j]
#                 subset.append(j)
            
#         if xor == target and len(subset) < least:
#             least = len(subset)
#             ans = subset
#     return ans

# def part1():
#     nbuts = []
#     for i, buts in enumerate(buttons): nbuts.append( [sum([2**( len(machines[i]) - x - 1) for x in but]) for but in buts] )
#     return sum( len(find_xors(sum(2**j for j, ch in enumerate(mach[-1::-1]) if ch == '#'), nbuts[i])) for i, mach in enumerate(machines) ) 


# def part2():
#     ans = 0
#     for i, jolts in enumerate(joltages):
#         buts = buttons[i]
        
#         A = [[0 for i_ in range(len(buts))] for j in range(len(jolts))]
#         for j, but in enumerate(buts):
#             for light in but:
#                 A[light][j] = 1

#         c = [1 for i_ in range(len(buts))]
#         res = scipy.optimize.linprog(c, A_eq=A, b_eq=jolts, integrality=1)

#         if not res.success:
#             print("Couldn't find optimal solution")
#             return -1

#         ans += sum(res.x)
#     return ans

# start = time.time()

# print(part1())
# print(part2())

# end = time.time()
# print(f"Took {(end - start) * 1000} ms")