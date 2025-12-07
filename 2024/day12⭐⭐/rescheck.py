from colorama import Fore
from pathlib import Path


dir = Path(__file__).parent.resolve()
file = Path(dir/'rescheck').resolve() # if not example else Path(dir/'example').resolve()

grid = {}

# for line in open(file).readlines():
#     char, ocur, _, __ = line.strip().split(' ')
#     # print( char, ocur)
#     if not char in grid.keys():
#         grid[char] = [0]
    
#     grid[char][0] += int(ocur)


# file = Path(dir/'input').resolve()

# for x, line in enumerate(open(file).readlines()):
#     for y, char in enumerate(line.strip()):
#         if len(grid[char]) == 1:
#             grid[char].append(0)
#             # print(grid[char])
#         grid[char][1] += 1


# for char, oc in grid.items():
#     if oc[0] != oc[1]:
#         print(Fore.RED,end='')
#     print(char, ': ', oc, Fore.RESET)
x = [i for i in range(8)]
x.append(x[0])
for i in range(0,8,2):
    print(x[i:i+3])