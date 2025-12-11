from pathlib import Path
from math import prod

example = True # False #  

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()
points = set()
for c in open(file).read().split('\n'):
    x,y = c.split(',')
    points.add((int(x),int(y)))


part1, part2 = 0, 0
part1 = max((abs(k[0] - l[0]) +1)*(abs(k[1] - l[1]) +1) for i, k in enumerate(points) for j, l in enumerate(points) if j > i)

area = set()
points.add(list(points)[0])
print('start area')
for i, st in enumerate(list(points)[:-1]):
    xs, ys = st
    xe, ye = list(points)[i+1]
    if xs == xe: area.update([(xs,y) for y in (range(ys,ye+1) if ys < ye else range(ye,ys+1))])
    else:        area.update([(x,ye) for x in (range(xs,xe+1) if xs < xe else range(xe,xs+1))])
print('end area')

def getRect(p1,p2):
    x1, y1 = p1
    x2, y2 = p2
    rect = set()
    rect.update([(x, y1) for x in (range(x1,x2+1) if x1 < x2 else range(x2,x1+1))])
    rect.update([(x, y2) for x in (range(x1,x2+1) if x1 < x2 else range(x2,x1+1))])
    rect.update([(x1, y) for y in (range(y1,y2+1) if y1 < y2 else range(y2,y1+1))])
    rect.update([(x2, y) for y in (range(y1,y2+1) if y1 < y2 else range(y2,y1+1))])
    return rect

print('start rect')
p2list = []

for i, p1 in enumerate(points):
    for j, p2 in enumerate(points):
        if j > i:
            isin = True
            for r in getRect(p1,p2): isin *= r in area
            if isin: p2list.append( (abs(p1[0] - p2[0]) +1)*(abs(p1[1] - p2[1]) +1) )

part2 = max(p2list)
sol1 = 50 if example else 4760959496
print(part1, (part1 == sol1) , part1 - sol1)

sol2 = 24 if example else 1537373473728
print(part2, (part2 == sol2) , part2 - sol2)  