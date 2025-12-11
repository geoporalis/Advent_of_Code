import bisect, itertools
from pathlib import Path

example = False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

# limit = 13 # max no. digits

# def solve(p: bool) -> int:
#     def rec(old: str):
#         if len(old) != limit // 2:
#             for d in bool(old) * "0" + "123456789":
#                 rec(new := old + d)
#                 for i in range(2, limit // len(new) + 1 if p else 3):
#                     s.add(int(i * new))

#     s = set(); rec("")
#     pre = [0, *itertools.accumulate(dp := sorted(s))]
#     return sum(pre[bisect.bisect_right(dp, b)] - pre[bisect.bisect_left(dp, a)]
#                for r in inp for a, b in [map(int, r.split("-"))])

# inp = open(file).read().split(",")
# print(f"silver: {solve(0)}, gold: {solve(1)}")  # -> silver: 29940924880, gold: 48631958998

from re import findall

print(*(sum(filter(lambda i: findall(rf'^(\d+)\1{r}$', str(i)),
    [id for lo, hi in findall(r'(\d+)-(\d+)', *open(file))
        for id in range(int(lo), int(hi)+1)])) for r in '$+'))