from pathlib import Path
from math import prod
from functools import cache

example = False # True # 
part1, part2 = 0, 0

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example.pt2').resolve()

inp = {"out": []}
for key, *values in map(str.split, open(file)):
    inp[key.strip(':')] = [v for v in values]

# @cache
# def findNext(knot:str,visit:tuple[int,int]):
#     if knot == 'out': return sum(visit) == 2
#     if knot == 'fft': visit = (1, visit[1])
#     if knot == 'dac': visit = (visit[0], 1)
#     return sum(findNext(k, visit) for k in inp[knot])
# part2 = findNext('svr', (0,0))

# @cache
# def np(v, d, f):
#     if v == 'out': return 1 if d and f else 0
#     return sum(np(w, d or v == 'dac', f or v == 'fft') for w in inp[v])

@cache
def p1(n): return (n=="out") + sum(map(p1,inp[n]))

@cache
def p2(n, df):
    cdf = df | (n=="dac")<<1 | (n=="fft")
    return (n=="out" and df==0x3) + sum(p2(c,cdf) for c in inp[n])

part1 = p1('you')
part2 = p2('svr', 0)

sol1 = 5 if example else 701
print(part1, (part1 == sol1) , part1 - sol1)
sol2 = 2 if example else 390108778818526 
print(part2, (part2 == sol2) , part2 - sol2)  