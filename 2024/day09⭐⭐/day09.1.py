from pathlib import Path
from colorama import Fore

import re

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() 
# file = Path(dir/'example').resolve()

oneline = [c for c in open(file).read()]   #.strip()


id=0
newline=[]
for idx in range(1,len(oneline)+1,2):
    for l in range(int(oneline[idx-1])):
        newline.append([id])
    try:
        for l in range(int(oneline[idx])):
            newline.append(['.'])
    except:
        pass
    id+=1
    # if id == 10:
    #     
newline = [n for n in newline if n != []]
# print(newline)
# newlist = list(newline)
# print("".join(newlist))
new_len = len(newline)
point_idx = [i for i in range(new_len) if newline[i] == ['.']]
num_idx = [i for i in range(new_len) if newline[i] != ['.']]

# print(point_idx[:10])
# print(num_idx[:10])

while True:
    j = point_idx.pop(0)
    i = num_idx.pop(-1)
    if i < j:
        break
    newline[i], newline[j] = newline[j], newline[i]
    print('\r', new_len,'/', i,'/', j, end='')

print()
# print("".join([str(n[0]) for n in newline]))
checksum = 0
idx = 0
while True:
    checksum += int(newline[idx][0])*idx
    idx+=1
    if newline[idx] == ['.']:
        break

print(checksum) 
# 90967962125 # too low
# 90994085674 # still too low

# 6390180901651 # * lists for the win

# example = 1928 // 1928
