from functools import cache
from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

def path(ss):
    (y,x), (Y,X) = [divmod('789456123_0A<v>'.find(t), 3) for t in ss]
    S = '>' * (X - x) + 'v' * (Y - y) + '0' * (y - Y) + '<' * (x - X)
    return S if (3,0) in [(y,X), (Y,x)] else S[::-1]

@cache
def length(S, d):
    if d < 0: return len(S)+1
    return sum(length(path(ss), d-1) for ss in zip('A' + S, S + 'A'))

for r in 2, 25:
    print(sum(int(S[:3]) * length(S[:3], r) for S in open(file)))