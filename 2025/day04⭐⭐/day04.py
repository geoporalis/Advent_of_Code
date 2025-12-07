from pathlib import Path
# import math, re

example = False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()
rows = open(file).read().split()

part1 = 0
part2 = 0
width = len(rows[0])
height= len(rows)

field = {(x,y): c   for x, l in enumerate(rows)
                    for y, c in enumerate(l)}
checks = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]


for (x,y), roll in field.items():
    if roll != "@": continue
    rolls = 0
    for check in checks:
        xc, yc = (x + check[0], y + check[1])
        if xc >= 0 and xc < height and yc >= 0 and yc < width and field[(xc,yc)] == '@': rolls +=1
    if rolls < 4: 
        part1 += 1

sol1 = 13 if example else 1424
# sol2 = 43 if example else 0
print(part1, (part1 == sol1) , part1 - sol1)
# print(part2, (part2 == sol2) , part2 - sol2)


