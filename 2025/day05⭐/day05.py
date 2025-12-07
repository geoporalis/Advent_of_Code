from pathlib import Path
from itertools import groupby

example =  False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()
ranges, ingredients = open(file).read().split('\n\n')

ranges = [r.split('-') for r in ranges.split() ]
ranges = [range(int(s),int(e)+1) for s,e in sorted(ranges, key = lambda r: r[0])]
ingredients = [int(i) for i in ingredients.split()]

def combineranges(i):
    for a, b in groupby(enumerate(i), lambda pair: pair[1] - pair[0]):
        b = list(b)
        yield range(b[0][1], b[-1][1]+1)



part1 = 0
# part1 = sum(1 for ingredient in ingredients for rang in ranges if ingredient in rang)
for ingredient in ingredients:
    for rang in ranges:
        if ingredient in rang:
            part1 += 1
            break

sol1 = 3 if example else 828
print(part1, (part1 == sol1) , part1 - sol1)

part2 = 0
it = 0
combined_ranges = [ranges[0]]
for r in ranges[1:]:
    for c in combined_ranges: 
    #     s |= set(c)
    # combined_ranges = []
    # for a, b in groupby(enumerate(s | set(r)),lambda pair: pair[1] - pair[0]):
    #     b = list(b)
    #     combined_ranges.append(range(b[0][1], b[-1][1]+1))
    
    # for r in combined_ranges:
    #     print(r)
    # print()
    # it+=1
    # print(it, end='\r')
    # s = set()

part2 = sum(len(r) for r in combined_ranges)

# x_ranges = []
# combined_ranges = ranges
# while(len(combined_ranges) != len(x_ranges)):
#     x_ranges = sorted(combined_ranges, key = lambda r: r[0])
#     combined_ranges = []
#     for i in range(len(x_ranges)-1):
#         combined_ranges += combineranges(set(x_ranges[i]) | set(x_ranges[i+1]))
    
    
    
    # for i in range(len(ranges)-1):
    #     combined_ranges = combineranges(set(ranges[i]) | set(ranges[i+1]))

# ranges = sorted(ranges, key = lambda r: r[0])
# for r in ranges: print(r)



#     for n in newranges:
#          newranges = combineranges(s)
# for t in combined_ranges: print(t)
# print(s)


# s = set()
# for r in ranges: s = s | set(r)
# part2 = len(s)
# new_ranges, old_ranges = [[int(r[0]), int(r[1])] for r in ranges], [int(ranges[0][0]), int(ranges[0][1])]







# old_ranges = [range(int(r[0]),int(r[1])) for r in ranges]
# new_ranges = old_ranges[0]
# for rang in old_ranges[1:]:
#     new_ranges = chain(new_ranges,rang)

# for part2, r in enumerate(old_ranges, 1): pass
# print(old_ranges)

# def inRange(rang, i, j): 
#     return (rang[0] <= i <= rang[1], rang[0] <= j <= rang[1]) 

# while(new_ranges != old_ranges):
#     old_ranges = new_ranges
#     new_ranges = [old_ranges[0]]
#     for [s, e] in old_ranges:
#         # if new_range != []: new_ranges.append(new_range)
#         # new_range = []
#         for n, rang in enumerate(new_ranges):
#             sinrange, einrange = inRange(rang, int(s), int(e))
#             print(rang, [s,e], sinrange, einrange)

#             if sinrange and einrange: continue
#             if not sinrange and einrange: rang[0] = int(s)
#             elif sinrange and not einrange: rang[1] = int(e)
#             elif int(s) < rang[0] and int(e) > rang[1]: rang = [int(s),int(e)]
#             elif not sinrange and not einrange: 
#                 new_range = [int(s),int(e)]
#                 new_ranges.append(new_range)

#     print("")            


# for rang in new_ranges:
#     print(rang)

# for [s, e] in new_ranges:
#     part2 += e-s+1

sol2 = 14 if example else 0
print(part2, (part2 == sol2) , part2 - sol2)         