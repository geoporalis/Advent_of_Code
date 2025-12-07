from pathlib import Path
from colorama import Fore
import numpy as np
from scipy.ndimage import rotate

import re

listOfData = []
dir = Path(__file__).parent.resolve()

aOD = []

with open(Path(dir/'input').resolve() ,'r') as f:
    input = f.read().replace("\n","O")

total_count = []
rowLen=input.find("O")

patternRow = r"(?=(XMAS))|(?=(SAMX))"
patternCol = r"(?=(X\w{"+str(rowLen+0)+ r"}M\w{"+str(rowLen+0)+ r"}A\w{"+str(rowLen+0)+ r"}S))|(?=(S\w{"+str(rowLen+0)+ r"}A\w{"+str(rowLen+0)+ r"}M\w{"+str(rowLen+0)+ r"}X))"
patternDup = r"(?=(X\w{"+str(rowLen+1)+ r"}M\w{"+str(rowLen+1)+ r"}A\w{"+str(rowLen+1)+ r"}S))|(?=(S\w{"+str(rowLen+1)+ r"}A\w{"+str(rowLen+1)+ r"}M\w{"+str(rowLen+1)+ r"}X))"
patternDdw = r"(?=(X\w{"+str(rowLen-1)+ r"}M\w{"+str(rowLen-1)+ r"}A\w{"+str(rowLen-1)+ r"}S))|(?=(S\w{"+str(rowLen-1)+ r"}A\w{"+str(rowLen-1)+ r"}M\w{"+str(rowLen-1)+ r"}X))"

count_a = len(re.findall(patternRow, input))
count_b = len(re.findall(patternCol, input))
count_c = len(re.findall(patternDup, input))
count_d = len(re.findall(patternDdw, input))

total_count.append(count_a)
total_count.append(count_b)
total_count.append(count_c)
total_count.append(count_d)

print(total_count, Fore.GREEN, sum(total_count), Fore.RESET)

patternCross =  r"(?=(M.M\w{"+str(rowLen-1)+ r"}A\w{"+str(rowLen-1)+ r"}S.S))|"
patternCross += r"(?=(S.S\w{"+str(rowLen-1)+ r"}A\w{"+str(rowLen-1)+ r"}M.M))|"
patternCross += r"(?=(S.M\w{"+str(rowLen-1)+ r"}A\w{"+str(rowLen-1)+ r"}S.M))|"
patternCross += r"(?=(M.S\w{"+str(rowLen-1)+ r"}A\w{"+str(rowLen-1)+ r"}M.S))"

count_x = len(re.findall(patternCross, input))

print(count_x)

# [419, 449, 851, 852]  2571