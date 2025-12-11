import re
from pathlib import Path

example =  False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

# ranges, ids = open(file).read().split("\n\n")
# ranges = [(int(a), int(b)) for a, b in re.findall(r"(\d+)-(\d+)", ranges)]
# ids = map(int, ids.split())

# def union(I, others):
#     a, b = I
#     rest = []
#     while others:
#         c, d = J = others.pop()
#         if b < c or a > d:
#             rest.append(J)
#         else:
#             a, b = min(a, c), max(b, d)
#             others += rest
#             rest = []
#     return (a, b), rest

# disjoint = []
# while ranges:
#     I, ranges = union(ranges.pop(), ranges)
#     disjoint.append(I)

# p1 = sum(any(a <= i <= b for a, b in disjoint) for i in ids)
# p2 = sum(b - a + 1 for a, b in disjoint)

# print(p1, p2)

I,J = open(file).read().strip().split("\n\n")
t, *R = sorted(tuple(map(int,i.split("-"))) for i in I.split("\n"))
print(sum(any(a <= int(i) <= b for (a,b) in [t]+R) for i in J.split("\n")))
print(__import__("functools").reduce(lambda a, r: a if r[1] <= a[1] else (a[0] + (r[1]-r[0]+1 if r[0]>a[1] else r[1]-a[1]), r[1]), R, (t[1]-t[0]+1,t[1]))[0])