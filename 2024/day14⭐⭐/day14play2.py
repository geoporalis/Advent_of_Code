import re, math
from colorama import Fore
from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

pattern = r'p=(\d{1,}),(\d{1,})\sv=(-?\d{1,}),(-?\d{1,})'

robots = [ {'px': int(claw[0]), 'py': int(claw[1]),
           'dx': int(claw[2]), 'dy': int(claw[3]),
           } for claw in re.findall(pattern, open(file).read())]

w = 11 if example else 101 # x-axis
h = 7 if example else 103 # y-axis

wq = w//2
wt = w//3
wm = w-wq-1
hq = h//2
ht = h//3
hm = h-hq-1

# print(wq, wm,'||', hq, hm)

def getQuadrant(nx, ny):
    # 4 tiled safety factor
    # if nx == (wm) or ny == (hm):
    #     return 0  
    # q = 1 if nx < wm else 2
    # q += 2 if ny > hm else 0

    # 9 tiled saftey factor
    q = 1 if nx < wt else 2 if wt < nx < 2*wt else 3
    q+= 0 if ny < ht else 3 if ht < ny < 2*ht else 6

    return q        

def moveRobot(robot, seconds):#%w, \
    nx, ny =    (robot['px'] + robot['dx']*seconds) % w, \
                (robot['py'] + robot['dy']*seconds) % h
    # return (nx, ny) # #
    return getQuadrant(nx, ny) #
# part 01

after100s = [moveRobot(robot, 8179) for robot in robots]

quads100s = [after100s.count(i) for i in range(0,9)]

print(quads100s, math.prod(quads100s[1:]))
# part 02

print(8179%101, (8179-99)/101)
secFac = []
minsf = 51**9
mini=0

for i in range(101*103):
    quads = [moveRobot(robot, i)  for robot in robots]    
    csf = [quads.count(j) for j in range(1,9) ]
    sf = math.prod(csf[1:])
    
    if sf < minsf:
        minsf= sf
        mini = i

print(mini, minsf)
# getAll = set()
# for robot in robots:
#     getAll.add(moveRobot(robot, 8080))
# for y in range(h):
#     for x in range(w):
    
#         if (x,y) in getAll:
#             print("#",end='')
#         else:
#             print(" ",end='')
#     print()

# 8886
# 8179

# part 02
# ? safety factory reciproc entropy ?
# ?variance 
# ?chinese remainder theroem
