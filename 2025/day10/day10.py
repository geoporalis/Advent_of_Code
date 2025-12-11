from pathlib import Path
from math import prod
from itertools import combinations

example = False # True #  

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

part1 = 0

for diagram, *buttons, joltage in map(str.split, open(file)):
    diagram = [c=='#' for c in diagram[1:-1]]
    buttons = [eval(b[:-1]+',)') for b in buttons]
    joltage = eval(joltage[1:-1])
    numbers = range(len(joltage))

    def toggle(buttons):
        for n in numbers:
            for pressed in combinations(buttons, n):
                if diagram == [sum(i in p for p in pressed)%2 for i in numbers]: return n
                # lights = [sum(i in p for p in pressed)%2 for i in numbers]
                # if lights == diagram: return n

                # lights=[]
                # for i in numbers:             # diagram/light positions
                #     li = 0
                #     for p in pressed:         # buttons of combinations
                #         li += i in p          # is diagram position in button
                #     lights.append(li%2)       # odd times pressed = true/on, even times pressed = false/off

    part1 += toggle(buttons)

sol1 = 7 if example else 475
print(part1, (part1 == sol1) , part1 - sol1)