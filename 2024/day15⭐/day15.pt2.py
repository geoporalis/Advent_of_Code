from colorama import Fore
from pathlib import Path

example = True  #False  #

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

free, crate, wall = '.', ['[',']'], '#'

areal, movesigns = open(file).read().split('\n\n')

moves = [directions[m] for m in movesigns.strip() if m != '\n']

# area = { (x,y): c for x, l in enumerate(areal.split('\n'))
#                  for y, c in enumerate(l.strip())}

area=  {}
x=0

for l in areal.split('\n'):
    y=0
    for c in l.strip():
        if c == '#':
            area[(x,y)] , area[(x,y+1)] = '#', '#' 
        if c == 'O':
            area[(x,y)] , area[(x,y+1)] = '[', ']'
        if c == '.':
            area[(x,y)] , area[(x,y+1)] = '.', '.'
        if c == '@':
            area[(x,y)] , area[(x,y+1)] = '@', '.'    
        y+=2
    x+=1


pos = [c for c, s in area.items() if s == '@'][0]

w, h = len([pos[0] for pos in area.keys() if pos[0] == 0 ]), len([pos[1] for pos in area.keys() if pos[1] == 0 ])

print(w,h)
area[pos] = free


def printArea():
    print(getkyfromval(mov), pos)
    print('   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0')
    for x in range(h):
        print(x, ' ', end='')
        for y in range(w):
            if (x,y) == pos:
                print('@ ',end='')
            else:
                # col = Fore.RED if area[(x,y)] == wall else Fore.YELLOW if area[(x,y)] == crate else Fore.BLACK
                # col, 
                print(area[(x,y)], Fore.RESET, end='')
        print()

mov = moves[0]
printArea()
# exit()


def canImoveThatCrateLR(pos, mov):
    nx, ny = pos[0]+mov[0], pos[1]+mov[1]
    if area[(nx, ny)] == wall:
        return
    if area[(nx, ny)] in crate:
        canImoveThatCrateLR((nx, ny), mov)
    if area[(nx, ny)] == free:
        area[(nx, ny)] = area[pos]
        area[pos] = free

def spreadTree(pos):
    if area[pos[0]] == ']' and area[(pos[0][0], pos[0][1]-1)] == '[':
        pos = [(pos[0][0], pos[0][1]-1)] + pos
    if area[pos[-1]] == '[' and area[(pos[-1][0], pos[-1][1]+1)] == ']':
        pos = [(pos[0][0], pos[0][1]+1)] + pos
    return pos

def canImoveThatTree(pos, mov):
    printArea() #print(pos)
    gear = [area[p] for p in pos]
    print("".join(gear))
    input()
    pass

def makeAmove(pos, mov):
    nx, ny = pos[0]+mov[0], pos[1]+mov[1]
    if area[(nx, ny)] == wall:
        return pos
    
    if area[(nx, ny)] in crate:
        if mov[0] == 0:
            canImoveThatCrateLR((nx, ny), mov)
        else:
            canImoveThatTree(spreadTree([(nx, ny)]), mov)
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


box_count = sum([cor[0]*100 +cor[1] for cor, box in area.items() if box == '['])

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

'''
part2
####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################
The sum of these boxes' GPS coordinates is 9021.
'''