import json, re
from colorama import Fore
from pathlib import Path

example =  False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

connCollection = {}
for c in open(file).readlines():
    con1, con2 = sorted(c.strip().split('-'))
    if not con1 in connCollection: connCollection |= {con1:[con2]} 
    else: connCollection[con1].append(con2)
    if not con2 in connCollection: connCollection |= {con2:[con1]} 
    else: connCollection[con2].append(con1)



lanparties = [ ]
for k, v in connCollection.items():
    v.append(k)
    lanparties.append(sorted(v))
#     if connCollection[party[:-1]]
# print(json.dumps(connCollection, indent=3))
biggest = dict()
for i, x in enumerate(lanparties):
    for j, y in enumerate(lanparties):
        if i != j:
            stack = ','.join(sorted(list(set(x).intersection(y))))
            if not stack in biggest: biggest[stack] = 0
            biggest[stack] += 1  

maxb = 0
score = ''
for big, times in biggest.items():
    leng = len(big.split(','))
    if times//leng == leng-1:
        if maxb < times:
            maxb = times
            score = big

print(score)
# answer: df,kg,la,mp,pb,qh,sk,th,vn,ww,xp,yp,zk
