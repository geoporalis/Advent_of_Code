import numpy as np
from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

# B = np.fromregex(file, r'-?\d+',
#     [('',int)]*4).view(int).reshape(-1,2,2)

# def f(D, M):
#     T = np.arange(M)
#     P = np.outer(T, D[:,1]) + D[:,0]
#     return (P%M).var(axis=1).argmin()

# W, H = 101, 103
# x, y = f(B[...,0], W), f(B[...,1], H)
# print((pow(W, -1, H) * (y-x) % H) * W + x)    # 8179  # correct

import re

w, h = 101, 103
bots = [[*map(int, re.findall(r'-?\d+',l))]
                   for l in open(file)]

def danger(t):
    a = b = c = d = 0

    for x, y, dx, dy in bots:
        x = (x + dx * t) % w
        y = (y + dy * t) % h

        a += x > w//2 and y > h//2
        b += x > w//2 and y < h//2
        c += x < w//2 and y > h//2
        d += x < w//2 and y < h//2

    return a * b * c * d

print(danger(100))                              # 232253028 # correct
print(min(range(10_000), key=danger))           # 8886      # false