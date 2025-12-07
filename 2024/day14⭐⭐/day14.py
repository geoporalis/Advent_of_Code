import re, math
from colorama import Fore
from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

pattern = r'p=(\d{1,}),(\d{1,})\sv=(-?\d{1,}),(-?\d{1,})'

margin = 10000000000000
robots = [ {'px': int(claw[0]), 'py': int(claw[1]),
           'dx': int(claw[2]), 'dy': int(claw[3]),
           } for claw in re.findall(pattern, open(file).read())]

w = 11 if example else 101 # x-axis
h = 7 if example else 103 # y-axis

wq = w//2
wm = w-wq-1
hq = h//2
hm = h-hq-1

# print(wq, wm,'||', hq, hm)

def getQuadrant(nx, ny):
    if nx == (wm) or ny == (hm):
        return 0  
    q = 1 if nx < wm else 2
    q += 2 if ny > hm else 0
        
    return q        

def moveRobot(robot, seconds):#%w, \
    nx, ny =    (robot['px'] + robot['dx']*seconds), (robot['py'] + robot['dy']*seconds) #%h

    while nx < 0: nx += w
    nx = nx%w

    while ny < 0: ny += h
    ny = ny%h

    return getQuadrant(nx, ny)  #
# part 01

after100s = [moveRobot(robot, 7700) for robot in robots]

quads100s = [after100s.count(i) for i in range(0,5)]

print(quads100s, math.prod(quads100s[1:])) # 232253028