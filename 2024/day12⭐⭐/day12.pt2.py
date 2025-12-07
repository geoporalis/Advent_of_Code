from colorama import Fore
from itertools import permutations
import math

from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

grid = { (x, y): {'char':c, 'xy':(x,y)} for x, l in enumerate(open(file).readlines()) 
                   for y, c in enumerate(l.strip()) }

corner_dict = {
    (True, True, True)      : 0,#'X',
    (True, True, False)     : 1,#'I',
    (True, False, True)     : 1,#'I',
    (True, False, False)    : 0,#'+',
    (False, True, True)     : 1,#'I',
    (False, True, False)    : 3,#'O',
    (False, False, True)    : 0,#'+',
    (False, False, False)   : 3,#'O',
    }

neigh_dist = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)] # 9 to get 4 sets of 3

def isFieldChar(char, field):
    try:
        return grid[field]['char'] == char
    except KeyError:
        return False

def getNeighbors(field):
    gn = [isFieldChar(grid[field]['char'], (field[0]+di[0], field[1]+di[1])) for di in neigh_dist]
    # print( field )
    # for  i, di in enumerate(neigh_dist):
    #     print(gn[i],'\t', (field[0]+di[0], field[1]+di[1]) , end='')
    #     try:
    #         print('\t',grid[(field[0]+di[0], field[1]+di[1])] )
    #     except:
    #         print(' ')
    return gn

    truNeighbors = []
    for di in neigh_dist:
        truNeighbors.append(isFieldChar(grid[field]['char'], (field[0]+di[0], field[1]+di[1])))
    truNeighbors.append(truNeighbors[0])
    return truNeighbors

def getFieldsCorners(field):
    # lt, rt, rb, lb = True, True, True, True
    truNeighbors = getNeighbors(field)
    corners = []
    for tre in range(0,8,2):
        mark = tuple(t for t in truNeighbors[tre:tre+3])
        # print(mark)
        corners.append(corner_dict[mark])
    # corners = [corner_dict[truNeighbors[tre:tre+3]] for tre in range(0,8,2)]
    # print(corners)
    # input()
    return corners  #[corner_dict[truNeighbors[tre:tre+3]] for tre in range(0,8,2)]

def getFieldsNeighbors(field):
    neigh = []
    for di in range(0,8,2):
        neighbor = (field[0]+neigh_dist[di][0], field[1]+neigh_dist[di][1])
        check = isFieldChar(grid[field]['char'], neighbor )
        neigh.append(neighbor if check else (None,None))
    return neigh

def getFieldsBorders(field):
    border = 0
    return border


for field, value in grid.items():

    neighbors = getFieldsNeighbors(field)
    borders = sum([1 for n in neighbors if n == (None, None)])
    grid[field] = {
        'char': value['char'],
        'xy':field,
        'corner': getFieldsCorners(field),
        'neigbours': neighbors,
        'borders': borders,
    }

# i=0    
# for key in grid.keys():   
#     print(key, grid[key])
#     i+=1
#     if i > 15:
#         break

group_char = {}
for key, plot in grid.items():
    if not plot['char'] in group_char:
        group_char[plot['char']] = []
    group_char[plot['char']].append(plot)

# print(group_char)
part1 = 0
part2 = 0
plotgroups = { char : [] for char in group_char}
for char, plots in group_char.items():
    for pnum, plot in enumerate(plots):
        gnum = -1
        for gn, gr in enumerate(plotgroups[char]):
            if plot in gr:
                gnum = gn
                break
        if gnum == -1:
            gnum=len(plotgroups[char])
            plotgroups[char].append([plot])
            # input(plotgroups[char])
        for pl2 in plots:
            if  math.dist(plot['xy'], pl2['xy']) == 1: # < 2:  #
                plotgroups[char][gnum].append(pl2)

    #merge groups
    mergedgroups = [plotgroups[char]]
    stillmerging = True

    while stillmerging:

        stillmerging = False
        for gnum1, group1 in enumerate(plotgroups[char]):
            for gnum2, group2 in enumerate(plotgroups[char]):
                if gnum1 == gnum2:
                    continue
                for pl in group2:
                    if pl in group1:
                        plotgroups[char][gnum1] += plotgroups[char].pop(gnum2)
                        stillmerging = True
                        break
                    #merge
                if stillmerging:
                    break
            if stillmerging:
                break

    #find duplicates
    singls=[]
    for groups in plotgroups[char]:
        singl = [ ]
        for plot1 in groups:
            if not plot1 in singl:
                singl.append(plot1)
        singls.append(singl)
    plotgroups[char]= singls
    # grouping should be done

    for gn, group in enumerate(plotgroups[char]):
        plotsfences = len(group)*4
        corners = 0
        borders = 0
        for plot in enumerate(group):
            # print(plot)
            corners += sum(plot[1]['corner'])
            borders += plot[1]['borders']
        part1border = len(group) * borders
        part2border = len(group) * corners //3
        part1 += part1border
        part2 += part2border

        print(char, len(group), borders, part1border, '||' , corners, part2border )

print('Answer1:', part1) # example: 1930 # input: 1477924 *
print('Answer2:', part2) # example: 1206 # input:  841934 *      # mr.crazy: 841934
