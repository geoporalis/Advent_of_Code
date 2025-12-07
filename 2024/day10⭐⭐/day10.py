# [ https://www.geeksforgeeks.org/python-program-for-depth-first-search-or-dfs-for-a-graph/ ]
# [ https://www.geeksforgeeks.org/dfs-traversal-of-a-tree-using-recursion/ ]

from colorama import Fore
from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

checksum = 0

area = { (x, y): lvl for y, line in enumerate(open(file).readlines()) 
                   for x, lvl in enumerate(line.strip()) }

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

trailheads = [xy for xy in area if area[xy]== '0']
# print('heads:', len(trailheads))
# trailtops = [xy for xy in area if area[xy]== '9']
# print('tops :', len(trailtops))


def findNextStep(xy, path):
    if area[xy] == '9':
        return [path]
    else:
        pfade = []
        for d in directions:
            xy_ = (xy[0] + d[0], xy[1] + d[1])
            if int(area.get(xy_, 0)) - int(area.get(xy)) == 1:
                pfade += findNextStep(xy_, path +  [xy_])
        return pfade

sammler = []
for xy in trailheads:
    sammler.append(findNextStep(xy, []))

trail9sum = 0 
for trails in sammler:
    # print(trails[-1], len(trails))
    trail9 = set()

    for trail in trails:
        trail9.add(trail[-1])
        if len(trail) == 9:
            checksum += 1
        #     print(Fore.GREEN, end='')
        # print(len(trail),Fore.RESET, trail)
    trail9sum += len(trail9)    

# print(len(sammler), sammler)


print('Anser 1: ', trail9sum) 
print('Anser 2: ', checksum) 

assert trail9sum == 36 if example else 709

assert checksum == 81 if example else 1326