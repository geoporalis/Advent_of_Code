from pathlib import Path
from math import prod

example = True # False #  

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

lights=[]
buttons=[]
joltage=[]
for line in open(file).read().split('\n'):
    light, rest = line.split('] (')
    button, jolt = rest.split(') {')
    lights.append([1 if l=='#' else 0 for l in light.strip('[') ])
    joltage.append([int(j) for j in jolt.strip('}').split(',')])
    buttons.append([[int(b) for bu in br.split(',') for b in bu ] for br in button.replace('(','').replace(')','').split(" ")])

for i, but in enumerate(buttons):
    print(lights[i],end=' ')
    for b in but: print(b, end=' ')
    print(joltage[i])

# part1, part2 = 0, 0


# sol1 = 50 if example else 4760959496
# print(part1, (part1 == sol1) , part1 - sol1)