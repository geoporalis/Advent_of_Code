from functools import cache
from pathlib import Path

example = True  #False # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()


P, _, *D = open(file).read().splitlines()

@cache
def count(d):
    return d == '' or sum(count(d.removeprefix(p))
        for p in P.split(', ') if d.startswith(p))

for type in bool, int:
    print(sum(map(type, map(count, D))))