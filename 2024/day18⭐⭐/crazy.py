from bisect import bisect
from pathlib import Path

example = False #True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

data = [*map(eval, open(file))]

def path(i):
    seen = {*data[:i]}
    todo = [(0, (0,0))]

    for dist, (x,y) in todo:
        if (x,y) == (70,70): return dist

        for x,y in (x,y+1), (x,y-1), (x+1,y), (x-1,y):
            if (x,y) not in seen and 0<=x<=70 and 0<=y<=70:
                todo.append((dist+1, (x,y)))
                seen.add((x,y))
    return 1e9

print(path(1024))

print(data[bisect(range(len(data)), 1e9-1, key=path)-1])