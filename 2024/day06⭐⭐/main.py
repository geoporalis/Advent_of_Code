from pathlib import Path
from colorama import Fore

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() 
example = Path(dir/'example').resolve()

lines = [l.strip() for l in open(file).readlines()]
# lines = [l.strip() for l in open().readlines()]

len_x = len(lines)
len_y = len(lines[0])

obstacle = '#'
direction = 0

def changeDirection(direction = direction):
    return (direction+1)%4


# print(changeDirection(3))

area = []
gy=-1
gx=-1
for x, row in enumerate(lines):
    if gy<0:
        gy = row.find('^')
        gx=x
    area.append([c for c in row.strip()])

def stillGuarding(gx=gx, gy=gy, area_x=len_x, area_y=len_y):
    return False if gx < 0 or gy < 0 or gx >= area_x or gy >=area_y else True  

def takeAStep(x,y, d=direction):
    if d == 0: #dir = up
        x-=1
    elif d == 1: #dir = right
        y+=1
    elif d == 2: #dir = down
        x+=1
    elif d == 3: #dir = left
        y-=1
    else:
        print('wrong direction')
        exit()
    return (x,y)
def printArea(area=area):
    x_count = 0
    for row in area:
        for col in row:
            if col == '.':
                print(Fore.LIGHTBLACK_EX, end='')
            elif col == obstacle:
                print(Fore.RED,end='')
            elif col == 'X':
                x_count += 1
                print(Fore.GREEN, end='')
            else:
                print(Fore.YELLOW,end='')
            print(col,end='')
        print('')
    # input('waiting')
    print(Fore.RESET)
    return x_count

step_count=0
while True:
    # direction_changed = False
    while True:    
        cx, cy = takeAStep(gx, gy, direction)
        try:
            if area[cx][cy] == changeDirection(direction):
                step_count += 1
        except:
            pass
        try:
            if area[cx][cy] == obstacle:
                direction = changeDirection(direction)
                # direction_changed = True
                # area[gx][gy] = '+'

                # printArea()
            else:
                [gx, gy] = [cx, cy]
                # step_count+=1
                break               
        except:
            [gx, gy] = [cx, cy]
            # step_count+=1
            break
        

    if not stillGuarding(gx, gy):
        break
    # if direction_changed:
    if direction == 0:
        area[gx][gy] = 0
    elif direction == 1:
        area[gx][gy] = 1
    elif direction == 2:
        area[gx][gy] = 2
    else:
        area[gx][gy] = 3

    #peek

print(printArea())
print(step_count)
# part 1: 5199
# part 2:
# 312 # to low

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# G = {i+j*1j: c for i,r in enumerate(open(file))
#                for j,c in enumerate(r.strip())}

# start = min(p for p in G if G[p] == '^')

# def walk(G):
#     pos, dir, seen = start, -1, set()
#     while pos in G and (pos,dir) not in seen:
#         seen |= {(pos,dir)}
#         if G.get(pos+dir) == "#":
#             dir *= -1j
#         else: pos += dir
#     return {p for p,_ in seen}, (pos,dir) in seen

# path = walk(G)[0]
# print(len(path))
# print(sum(walk(G | {o: '#'})[1] for o in path))

#~~~~~~~~~~~~~~~~~~~~~
inp = open(file).read() #utils.get_input(day=6)
sample_inp = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
# inp = sample_inp
# DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# d = 0

# rows = inp.strip().split("\n")

# # This is abusive, please don't do this
# INDICES = {x: {y: 0 for y in range(len(rows))} for x in range(len(rows[0]))}

# pos = None
# walls = set()
# for x, row in enumerate(rows):
#     for y, c in enumerate(row):
#         if c == "#":
#             walls.add((x, y))
#         if c == "^":
#             pos = (x, y)
# assert pos is not None

# def traverse_map(walls, spos):
#     seen = {(spos, 0)}
#     pos = spos
#     d = 0
#     try:
#         while True:
#             pos_ = (pos[0] + DIRS[d][0], pos[1] + DIRS[d][1])
#             if pos_ in walls:
#                 d = (d + 1) % 4
#                 continue
#             INDICES[pos_[0]][pos_[1]]
#             if (pos_, d) in seen:
#                 return None
#             seen.add((pos_, d))
#             pos = pos_
#     except KeyError:
#         return seen

# seen = traverse_map(walls, pos)
# assert seen is not None
# allseen = set(p[0] for p in seen)
# print(len(allseen))#, day=6, append=0, w=1)

# impossible = 0
# for p in allseen:
#     if p in walls or p == pos:
#         continue
#     if traverse_map(walls.union({p}), pos) is None:
#         impossible += 1
# print(impossible)#, day=6, append=1, w=1)