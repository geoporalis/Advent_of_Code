from pathlib import Path
from math import prod

example = False # True # 
part1, part2 = 0, 0

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example.pt1').resolve()

inp = {}
for key, *values in map(str.split, open(file)):
    inp[key.strip(':')] = [v for v in values]

def findNext(knot):
    return 1 if knot == 'out' else sum(findNext(k) for k in inp[knot])

part1 = findNext('you')
sol1 = 5 if example else 701
print(part1, (part1 == sol1) , part1 - sol1)

# part2 = prod(p2)
# sol2 = 2 if example else 1537373473728
# print(part2, (part2 == sol2) , part2 - sol2)  