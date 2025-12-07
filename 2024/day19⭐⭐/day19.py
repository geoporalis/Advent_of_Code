# from functools import cache
from pathlib import Path

example = False # True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

# patterns, designs = open(file).read().split('\n\n')
patterns, _, *designs = open(file).read().splitlines()

patterns = patterns.split(', ')
print(len(designs))

def match(design):
    if design == '': return 1
    for p in patterns:
        if design.startswith(p):
            if match(design.removeprefix(p)):
                return 1
    return False

# @cache
cache = dict()
def count(design):
    if design in cache:
        return cache[design]
    if design == "": return 1 
    matchs = 0
    for p in patterns: 
        if design.startswith(p):
            matchs += count(design.removeprefix(p))
    cache[design] = matchs
    return matchs


part1, miss1 = 0, 0
part1 = sum(map(match, designs))
print("Answer1:", part1) 

part2 = sum(map(count, designs))
print("Answer2:", part2) 
# for design in designs: #[:1]:

#     if match(design):
#         part1+=1
#     else:
#         miss1+=1

# print("Answer1:", miss1, miss1+part1)
# example: 6 
# input: 318? too high 
#        150  too low
#        315 *

# pt2
# example: 16
# input: 625108891232249


# crazy 315
# 625108891232249