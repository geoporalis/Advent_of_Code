from pathlib import Path
from colorama import Fore

import re

listOfData = []
dir = Path(__file__).parent.resolve()

with open(Path(dir/'input').resolve() ,'r') as f:
    listOfData = ("").join([x.strip("\n") for x in f.readlines()])

listOfData = ("").join([x.split("don't()")[0] for x in listOfData.split('do()')   ])

x = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", listOfData)
save_reports = sum([int(i) * int(j) for i,j in x ])

print(Fore.GREEN, save_reports, Fore.RESET)
