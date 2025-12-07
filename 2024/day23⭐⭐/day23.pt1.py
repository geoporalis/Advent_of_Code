import json, re
from colorama import Fore
from pathlib import Path

example =  True  # False # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

connCollection = {}
for c in open(file).readlines():
    con1, con2 = c.strip().split('-')
    if not con1 in connCollection: connCollection |= {con1:[con2]} 
    else: connCollection[con1].append(con2)
    if not con2 in connCollection: connCollection |= {con2:[con1]} 
    else: connCollection[con2].append(con1)

triplesets = set()
for fk, fv in connCollection.items():
    for sk in fv:
        for tk in connCollection[sk]:
            if tk in fv:
                triplesets.add(','.join(sorted([fk, sk, tk])))

tcount = 0
for trip in triplesets:
    if len(re.findall(r'(t[a-z])',trip)) > 0:
        print(Fore.GREEN, end='')
        tcount+=1
        print(trip, Fore.RESET)

print(tcount)
# input: 2376 # too high, check only for left t's
#        1327 
