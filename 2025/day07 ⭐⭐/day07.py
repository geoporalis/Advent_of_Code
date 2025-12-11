from pathlib import Path
import math

example = False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()
lines = open(file).read().split('\n')
start = [i for i, l in enumerate(lines[0]) if l == 'S']

part1, part2 = 0, 0

index={start[0]:1}
for l in lines[1:]:
    nextidx = {}
    for idx, beams in index.items():
        if l[idx] == '^': 
            for idxx in [idx-1, idx+1]:
                if idxx in nextidx.keys(): nextidx[idxx] += beams
                else: nextidx[idxx] = beams
            part1 += 1
        else: 
            if idx in nextidx.keys(): nextidx[idx] += beams
            else: nextidx[idx] = beams
    index = nextidx

part2 = sum(i for k,i in index.items())

sol1 = 21 if example else 1507
print(part1, (part1 == sol1) , part1 - sol1)

sol2 = 40 if example else 1537373473728
print(part2, (part2 == sol2) , part2 - sol2)  