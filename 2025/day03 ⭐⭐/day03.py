from pathlib import Path
# import math, re

example = True # False # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

part1 = 0
part2 = 0
lines = [r for r in open(file).readlines() ]

for l in lines:
    joltage = 0
    for idx, i in enumerate(l):
        for jdx, j in enumerate(l):
            if idx == jdx: continue
            n = int(i+j) if idx<jdx else int(j+i)
            if n > joltage: joltage = n
    print(joltage)        
    part1 += joltage


sol1 = 357 if example else 17074
sol2 = 3121910778619 if example else 0
print(part1, (part1 == sol1) , part1 - sol1)
print(part2, (part2 == sol2) , part2 - sol2)


