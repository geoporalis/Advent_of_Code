from colorama import Fore
from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()
# file = Path(dir/'exsol').resolve()

# directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
directions = {'^':(-1, 0), 
              '>':( 0, 1),
              'v':( 1, 0),
              '<':( 0,-1)}

def getkyfromval(mov):
    return [k for k,v in directions.items() if v == mov][0]

free, crate, wall = '.', 'O', '#'
areal, movesigns = open(file).read().split('\n\n')

moves = [directions[m] for m in movesigns.strip() if m != '\n']

area = { (x,y): c for x, l in enumerate(areal.split('\n'))
                 for y, c in enumerate(l.strip())}
pos = [c for c, s in area.items() if s == '@'][0]
w, h = len([pos[0] for pos in area.keys() if pos[0] == 0 ]), len([pos[1] for pos in area.keys() if pos[1] == 0 ])
print(w,h)
area[pos] = free

def printArea():
    print(getkyfromval(mov))
    for x in range(h):
        for y in range(w):
            if (x,y) == pos:
                print('@',end='')
            else:
                col = Fore.RED if area[(x,y)] == wall else Fore.YELLOW if area[(x,y)] == crate else Fore.BLACK
                print(col, area[(x,y)], Fore.RESET, end='')
        print()

def canImoveThatCrate(pos, mov):
    nx, ny = pos[0]+mov[0], pos[1]+mov[1]
    if area[(nx, ny)] == wall:
        return False
    if area[(nx, ny)] == crate:
        canImoveThatCrate((nx, ny), mov)
        # if not canImoveThatCrate((nx, ny), mov):
        #     return False
    if area[(nx, ny)] == free:
        area[(nx, ny)] = crate
        area[pos] = free
    #     return True
    # else:
    #     return False

def makeAmove(pos, mov):
    nx, ny = pos[0]+mov[0], pos[1]+mov[1]
    if area[(nx, ny)] == wall:
        return pos
    if area[(nx, ny)] == crate:
        canImoveThatCrate((nx, ny), mov)
        # if not canImoveThatCrate((nx, ny), mov):
        #     return pos
    if area[(nx, ny)] == free:
        pos = (nx, ny)
    return pos

for mov in moves:
    # print(pos, mov, end=' -> ')
    pos = makeAmove(pos, mov)
    # printArea()
    # input()


box_count = sum([cor[0]*100 +cor[1] for cor, box in area.items() if box == 'O'])

print(box_count) # 2028 for small # 10092 for large example
# 1413675
'''
large: #10092
##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########

small:  #2028
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########
'''