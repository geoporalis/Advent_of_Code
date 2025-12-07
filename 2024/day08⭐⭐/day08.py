from colorama import Fore
from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()


grid = {}
goords = set()
for x, line in enumerate(open(file).readlines()):
    for y, char in enumerate(line.strip()):
        if not char in grid.keys():
            grid[char] = []
        grid[char] += [(x,y)]
        goords.add((x,y))
        w=y
    h=x

def calcNewCoords(coord1, coord2):
    xy = set()
    x1, y1 = coord1
    x2, y2 = coord2
    x3, y3 = 2*x1-x2, 2*y1-y2
    if 0 <= y3 <= h and 0 <= x3 <= w:
      xy.add((x3, y3))
    return xy

def calcHarmonics(coord1, coord2):
    xy = set()
    x1, y1 = coord1
    x2, y2 = coord2
    dx, dy = x1-x2, y1-y2
    i=0
    while True:
        x3, y3 = x1+dx*i, y1+dy*i
        if 0 <= y3 <= h and 0 <= x3 <= w:
            xy.add((x3, y3))
            i+=1
        else: break
    return xy

part1 = set()
part2 = set()
for k, ants in grid.items():
    if k == '.': continue

    for ant1 in ants:
        for ant2 in ants:
            if ant1 == ant2: continue
            part1 |= (calcNewCoords(ant1, ant2))
            part2 |= (calcHarmonics(ant1, ant2))

print('Answer1: ',len(part1))    
print('Answer1: ',len(part2))    



# file = Path(dir/'exsol').resolve()
# nodcount = 0
# for l in open(file).readlines():
#     for c in l:
#         if c=='#': nodcount += 1
# print('\n',nodcount)
     
