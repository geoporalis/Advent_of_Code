from pathlib import Path
from colorama import Fore
import numpy as np

import re

listOfData = []
dir = Path(__file__).parent.resolve()

aOD = []

with open(Path(dir/'input').resolve() ,'r') as f:
    listOfData = f.readlines()
    for line in listOfData:
        aOD.append([char for char in line.strip("\n")])

total_count = []
count_a = 0
count_b = 0
count_c = 0
count_d = 0
for c in range(0,len(aOD)):    #
    for r in range(0,len(aOD)):
        try:
            test = "".join([aOD[c][r+0],
                            aOD[c][r+1],
                            aOD[c][r+2],
                            aOD[c][r+3],
                            ])
            count_a += 1 if test == 'XMAS' or test == 'SAMX' else 0
        except:
            pass
        try:
            test = "".join([aOD[c+0][r],
                            aOD[c+1][r],
                            aOD[c+2][r],
                            aOD[c+3][r],
                            ])
            count_b += 1 if test == 'XMAS' or test == 'SAMX' else 0
        except:
            pass
        try:
            test = "".join(
                [aOD[c+0][r+0],
                aOD[c+1][r+1],
                aOD[c+2][r+2],
                aOD[c+3][r+3]]
            )
            count_c += 1 if test == 'XMAS' or test == 'SAMX' else 0
        except:
            pass
        try:
            test = "".join(
                [aOD[c+0][r+3],
                aOD[c+1][r+2],
                aOD[c+2][r+1],
                aOD[c+3][r+0]]
            )
            count_d += 1 if test == 'XMAS' or test == 'SAMX' else 0
        except:
            pass

total_count.append(count_a)
total_count.append(count_b)
total_count.append(count_c)
total_count.append(count_d)

print(total_count, Fore.GREEN, sum(total_count), Fore.RESET)

# patternRow = '(?=(XMAS))|(?=(SAMX))'
# patternCol =    '(?=(X\w{' +str(rowLen-1)+'}M\w{' +str(rowLen-1)+'}A\w{' +str(rowLen-1)+'}S\w{' +str(rowLen-1)+'}))| \
#                  (?=(S\w{' +str(rowLen-1)+'}A\w{' +str(rowLen-1)+'}M\w{' +str(rowLen-1)+'}X\w{' +str(rowLen-1)+'}))'