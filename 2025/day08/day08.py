# We can find the euclidian distance with the equation: 
# d = sqrt((px1 - px2)^2 + (py1 - py2)^2 + (pz1 - pz2)^2)

from pathlib import Path
from math import sqrt

example = True # False # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()
lines = open(file).read().split('\n')
boxes = []

for line in lines:
    x,y,z = line.split(',')
    boxes.append({'x':int(x), 'y':int(y),'z':int(z)})

distances = []
for i, boxi in enumerate(boxes):
    boxxes = []
    for j, boxj in enumerate(boxes):
        if j > i: dist = boxxes.append({'eud':int(sqrt((boxi['x'] - boxj['x'])**2 + (boxi['y'] - boxj['y'])**2 + (boxi['z'] - boxj['z'])**2)),
                                        'i':boxi,
                                        'j':boxj}) 
        # else: dist=0
        # boxxes.append(int(dist))
    if len(boxxes) > 0 :distances.append(boxxes)

for dist in distances:
    print(dist)

part1, part2 = 0, 0