from pathlib import Path

example = False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example.pt1').resolve()

# game = { line.split(':')[0]: line.split(':')[1].split() for line in open(file).read().split('\n') if line }

# memo = {}
# def count_paths(node, dac=False, fft=False):
#     if node == 'out': return 1 if dac and fft else 0
#     if node == 'dac': dac = True
#     if node == 'fft': fft = True
#     key = (node, dac, fft)
#     if key not in memo:
#         memo[key] = sum(count_paths(n, dac, fft) for n in game[node])
#     return memo[key]

# print(f"Part1: {count_paths('you', True, True)}")
# print(f"Part2: {count_paths('svr')}")

# from functools import*
# z=cache(lambda x,t,g={l[:3]:l[4:].split()for l in open(file)}:sum(z(v,t+(x in'dac fft'))for v in g[x])if x in g else t>1)
# print('Part 1:',z('you',2),'\nPart 2:',z('svr',0))

from functools import cache

G = {k[:-1]:v for k,*v in map(str.split, open(file))} | {'out':[]}

@cache
def count(here, dest):
    return here == dest or sum(count(next, dest) for next in G[here])

print(count('you', 'out'))
print(count('svr', 'fft') * count('fft', 'dac') * count('dac', 'out'))