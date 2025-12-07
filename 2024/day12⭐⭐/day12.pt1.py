from colorama import Fore
from itertools import permutations
import math

from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

grid = {}

for x, line in enumerate(open(file).readlines()):
    for y, char in enumerate(line.strip()):
        if not char in grid.keys():
            grid[char] = []
        grid[char] += [[(x,y),4]]

part1 = 0
fences = 0
plotgroups = { char : [] for char in grid.keys()}
for char, plots in grid.items():
    for  p, pl1 in enumerate(plots):
        gnum = -1
        for gn, gr in enumerate(plotgroups[char]):
            if pl1 in gr:
                gnum = gn
                break
        if gnum == -1:
            gnum=len(plotgroups[char])
            plotgroups[char].append([pl1])
            # input(plotgroups[char])
        for pl2 in plots:
            if  math.dist(pl1[0], pl2[0]) == 1: # < 2:  #
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


    for gn, group in enumerate(plotgroups[char]):
        plotsfences = len(group)*4
        for  pn1, pl1 in enumerate(group):
            for  pn2, pl2 in enumerate(group):
                if  math.dist(pl1[0], pl2[0]) == 1:
                    plotsfences-= 1  
        groupfences = len(group) *  plotsfences
        part1 += groupfences
        print(char, len(group), plotsfences, groupfences )
    #             plots[p][1] -= 1 
    # plotsfences = sum(p[1] for p in plots)
    # for pl in permutations(plots, 2):
    #     input(pl)
        # d = math.dist(pl1[0], pl2[1])
        # if d == 1:
        #     plotsfences -=1
            # print(1, end = ' ')
            # print(pl1, pl2)



    # part1 += plotsfences
    # print(char, len(plots), plotsfences )
# for pl in plotgroups['C']:
#     print(len(pl))
#     print(pl, '\n')
# print()
# for pl in plotgroups['F']:
#     print(len(pl))
#     print(pl, '\n')

print(Fore.RED,'Answer1: ',Fore.GREEN,part1,Fore.RESET)   #1930
# 1486368 # too high
# 1477924 *

'''
R   12  18  216 
I    4   8   32
I   14  22  308
C   14  28  392
C    1   4    4
F   10  18  180
V   13  20  260
J   11  20  220
E   13  18  234
M    5  12   60
S    3   8   24
'''