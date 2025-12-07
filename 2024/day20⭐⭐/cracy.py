from itertools import combinations
from pathlib import Path

example = False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

grid = {i+j*1j: c for i,r in enumerate(open(file))
                  for j,c in enumerate(r) if c != '#'}

start, = (p for p in grid if grid[p] == 'S')


dist = {start: 0}
todo = [start]

for pos in todo:
    for new in pos-1, pos+1, pos-1j, pos+1j:
        if new in grid and new not in dist:
            dist[new] = dist[pos] + 1
            todo += [new]


a = b = 0

for (p,i), (q,j) in combinations(dist.items(), 2):
    d = abs((p-q).real) + abs((p-q).imag)
    if d == 2 and j-i-d >= 100: a += 1
    if d < 21 and j-i-d >= 100: b += 1

print(a, b)