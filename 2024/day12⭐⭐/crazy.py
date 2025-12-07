from pathlib import Path

example = True  #False  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

grid = {i+j*1j: c for i,r in enumerate(open(file))
                  for j,c in enumerate(r.strip())}

sets = {p: {p} for p in grid}

for p in grid:
    for n in p+1, p-1, p+1j, p-1j:
        if n in grid and grid[p] == grid[n]:
            sets[p] |= sets[n]
            for x in sets[p]: 
                sets[x] = sets[p]

sets = {tuple(s) for s in sets.values()}

def edge(ps):
    P = {(p,d) for d in (+1,-1,+1j,-1j) for p in ps if p+d not in ps}
    return P, P - {(p+d*1j, d) for p,d in P}

for part in 0,1: print(sum(len(s) * len(edge(s)[part]) for s in sets))

# from numpy import array as A, unique as uniq
# from scipy.ndimage import label
# from scipy.signal import convolve2d

# G = A([list(l.strip()) for l in open(0)])
# S = lambda A: abs(A).sum()

# ans = A([0,0])
# for L, n in [label(G==g) for g in uniq(G)]:
#     for i in range(n):
#         H = (L == i+1)

#         h = convolve2d(H, [[1,-1]])
#         v = convolve2d(H, [[1],[-1]])
#         x = convolve2d(H, [[-1,1],[1,-1]])

#         ans += S(H) * A([S(h)+S(v), S(x)])

# print(*ans)

