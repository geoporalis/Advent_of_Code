from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()

file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

checksum = 0

stones = open(file).readlines()[0].strip()

from functools import cache
from math import floor, log10

@cache
def count(x, d=75):
    if d == 0: return 1
    if x == 0: return count(1, d-1)

    l = floor(log10(x))+1
    if l % 2: return count(x*2024, d-1)

    return (count(x // 10**(l//2), d-1)+
            count(x %  10**(l//2), d-1))

data = map(int, open(file).read().split())
print(sum(map(count, data)))

# import functools

# @functools.cache
# def count( n, b ):
#     if b == 75:
#         return 1
#     if n == 0:
#         return count( 1, b + 1 )
#     ns = str( n )
#     nl = len( ns )
#     if nl & 1 == 0:
#         return ( count( int( ns[ : nl // 2 ] ), b + 1 ) +
#                  count( int( ns[ nl // 2 : ] ), b + 1 ) )
#     return count( n * 2024, b + 1 )

# print( sum( count( int( n ), 0 ) for n in open( 0 ).read().split() ) )

# from collections import defaultdict
# # from aoc import nums, read_input

# lines = open(file).readlines()[0].strip()   # read_input(split_lines=False)
# stones = {n: 1 for n in lines.split()}
# print(stones)

# def blink(stones):
#     new_stones = defaultdict(int)
#     for stone, count in stones.items():
#         if stone == 0:
#             new_stones[1] += count
#         elif len(str(stone)) % 2 == 0:
#             s = str(stone)
#             lh, rh = s[: len(s) // 2], s[len(s) // 2 :]
#             new_stones[int(lh)] += count
#             new_stones[int(rh)] += count
#         else:
#             new_stones[stone * 2024] += count
#     return new_stones


# p1 = stones.copy()
# for i in range(25):
#     p1 = blink(p1)
# print(sum(p1.values()))

# p2 = stones.copy()
# for i in range(75):
#     p2 = blink(p2)
# print(sum(p2.values()))