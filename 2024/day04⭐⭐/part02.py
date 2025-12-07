from pathlib import Path
from colorama import Fore

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
for c in range(0,len(aOD)):  
    for r in range(0,len(aOD)):
        try:
            test = "".join([aOD[c+0][r+0],
                            aOD[c+1][r+1],
                            aOD[c+2][r+2],
                            ])
            test2= "".join([aOD[c+2][r+0],
                            aOD[c+1][r+1],
                            aOD[c+0][r+2],
                            ])
            
            count_a += 1 if (test == 'MAS' or test == 'SAM') and (test2 == 'MAS' or test2 == 'SAM') else 0
        except:
            pass

total_count.append(count_a)

print(total_count, Fore.GREEN, sum(total_count), Fore.RESET)

# [1993]  1993 too high
# [1992]  1992 lol