from pathlib import Path

example =  False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()
ranges, ingredients = open(file).read().split('\n\n')

ranges = [r.split('-') for r in ranges.split() ]
ranges = [[int(s),int(e)+1] for s,e in sorted(ranges, key = lambda r: r[0])]
ingredients = [int(i) for i in ingredients.split()]

combined_ranges = [ranges[0]]
for r in ranges[1:]:
    for ci, c in enumerate(combined_ranges):
        if r[0] in range(c[0],c[1]):
            if r[1] > c[1]: combined_ranges[ci][1] = r[1]
            break
        else: 
            if ci+1 == len(combined_ranges): combined_ranges.append([r[0],r[1]])

part1 = sum(1 for ingredient in ingredients for rang in combined_ranges if ingredient in range(rang[0],rang[1]))
part2 = sum(len(range(r[0],r[1])) for r in combined_ranges)

sol1 = 3 if example else 828
print(part1, (part1 == sol1) , part1 - sol1)
sol2 = 14 if example else 0
print(part2, (part2 == sol2) , part2 - sol2)         