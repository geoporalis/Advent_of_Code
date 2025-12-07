from pathlib import Path
from colorama import Fore

import re

example = False  #True  #

dir = Path(__file__).parent.resolve()

file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

oneline = [c for c in open(file).read()]  

id=0
newline=[]
toggler = True

for o in oneline:
    if int(o) > 0:
        if toggler:
            newline.append([id, int(o)])
            id+=1
        else:
            newline.append(['.', int(o)])
    toggler = False if toggler else True
    
def newIdx(line_list):
    return [i for i in range(len(line_list)) if line_list[i][0] == '.'], \
           [i for i in reversed(range(len(line_list))) if line_list[i][0] != '.']

point_idx, num_idx = newIdx(newline)

num_x = 0

while True:
    try:
        num = num_idx[num_x]
        num_siz = newline[num][1]
        for poi in point_idx:
            change = False
            if poi >= num:
                break
            poi_siz = newline[poi][1]
            if num_siz <= poi_siz: #
                change = True
                newline[num], newline[poi] = newline[poi], newline[num]
                res = poi_siz - num_siz
                if res > 0:
                    newline[num][1] = poi_siz - res
                    newline.insert(poi+1, [newline[num][0], res])
                break
        if change:
            point_idx, num_idx = newIdx(newline)
        else:
            num_x+=1
        print('\r', len(num_idx), num_x, end='')
    except:
        break
print()

checksum = 0
idx = -1

if example:
    defreged = ''.join([''.join([str(x)]*y) for x, y in newline])
    print(defreged)
    assert defreged == '00992111777.44.333....5555.6666.....8888..'

for x, y in newline:
    for t in range(y):
        idx+=1
        if x == '.':
            continue
        checksum += x*idx

print('Anser: ', checksum) 

assert checksum == 2858 if example else 6412390114238
 
# 6412390114238 # says crazy +1
#   86453151529 # too low
