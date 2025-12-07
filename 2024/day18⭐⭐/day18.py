import re
from pathlib import Path

example = False # True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

dtat = [tuple(map(int , re.findall(r'-?\d+',l))) for l in open(file).readlines()]

def path(limit):
    seen = {*dtat[:limit]}
    todo = [(0, (0,0))]
    for d, (x, y) in todo:
        if (x,y) == (70,70): return d
        for x,y in (x,y+1), (x,y-1), (x+1,y), (x-1,y):
            if (x,y) not in seen and 0<=x<=70 and 0<=y<=70:
                todo.append((d+1, (x,y)))
                seen.add((x,y))
    return 1e23

print(path(1024))  

for l in range(1024,len(dtat)):
    if path(l) == 1e23:
        print(l-1, dtat[l-1])
        break