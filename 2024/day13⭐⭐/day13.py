# from colorama import Fore
# from itertools import permutations
# import math
import matplotlib.pyplot as plt
import re

from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

pattern = r'Button\sA:\sX\+(\d\d),\sY\+(\d\d)\nButton\sB:\sX\+(\d\d),\sY\+(\d\d)\nPrize:\sX=(\d*),\sY=(\d*)'

margin = 10000000000000

claws = [ {'AX': int(claw[0]), 'AY': int(claw[1]), 'AK': int(claw[1])/int(claw[0]), 
           'BX': int(claw[2]), 'BY': int(claw[3]), 'BK': int(claw[3])/int(claw[2]), 
           'PX': int(claw[4])+margin, 'PY': int(claw[5])+margin, 'PK': (int(claw[5])+margin)/(int(claw[4])+margin),
           } for claw in re.findall(pattern, open(file).read())]

# print(claws[0])

def checkThePrize(claw):
    tokens = [0]
    print()
    for a in reversed(range(claw['PX']//claw['AX'])):
        if (claw['PX'] - a*claw['AX'])%claw['BX'] == 0:
            b = (claw['PX']- a*claw['AX'])/claw['BX']
            if a*claw['AY'] + b*claw['BY'] == claw['PY']:
                tokens.append(a*3+b)


# fig, ax = plt.subplots()

# xr = range(0,200,10)
# y = [x * claws[0]['AY']/claws[0]['AX'] for x in xr]
# y2= [x * claws[0]['BY']/claws[0]['BX'] for x in xr]

# ax.plot(xr, y , color='C3', label='A')
# ax.plot(xr, y2, color='C0', label='B')
# ax.plot(94,34,'rx')
# ax.plot(94*2,34*2,'rx')

# ax.plot(22,67,'bx')
# # ax.plot(8400,5400,'ro')
# # ax.axline((1, 8000), slope=0.361)
# # ax.axline((1, 8000), slope=0.361)

# ax.legend()

# plt.show()
newer_ever = []
not_exactly= []
grand_total = 0
for i, claw in enumerate(claws):

    BY0 = claw['PY'] - claw['BK'] * claw['PX']
    SX = (claw['PY'] - claw['BK'] * claw['PX']) / (claw['AK'] - claw['BK'])
    SY = claw['AK'] * SX
    claw['SX'] = SX
    claw['SY'] = SY

    if claw['AK'] > claw['PK'] and claw['BK'] > claw['PK']:
        newer_ever.append(claw)
        continue
    if (claw['AK'] + claw['BK']) < claw['PK']:
        newer_ever.append(claw)
        continue

    if ( 
        round(SX / claw['AX'],2)%1 != 0.0  or
        round(SY / claw['AY'],2)%1 != 0.0  or
        round((claw['PX']-SX) / claw['BX'],2)%1 != 0.0  or
        round((claw['PY']-SY) / claw['BY'],2)%1 != 0.0 
        ):  
        not_exactly.append(claw)
        continue

    print(   round(SX / claw['AX'],2),  round((claw['PX']-SX) / claw['BX'],2))
    tokens = round(SX / claw['AX'],2)*3 + round((claw['PX']-SX) / claw['BX'],2)*1
    print(tokens)
    grand_total += tokens
print('Answer1:', grand_total)
    # plt.figure()
    # xr = range(0,9000,100)
    # y = [x * claw['AK'] for x in xr]
    # y2= [x * claw['BK'] + BY0 for x in xr]    
    # plt.plot(xr, y , color='C3', label='A')
    # plt.plot(xr, y2, color='C0', label='B')
    # plt.plot(claw['AX'],claw['AY'],'rx')
    # plt.plot(claw['BX'],claw['BY'],'bx')
    # plt.plot(claw['PX'],claw['PY'],'gx')
    # plt.plot(claw['SX'],claw['SY'],'yx')

# plt.show()


# print('not:',not_exactly)
# print('newer:', newer_ever)
        #super

    


# 
#     print('AK', claw['AY']/ claw['AX'])
#     print('BK', claw['BY']/ claw['BX'])







    # print()

# iWon = [checkThePrize(claw) ]

# for claw in claws:  #[:1]:
# a*claw['AX'] + b*claw['BX'] = claw['PX']
# a*claw['AY'] + b*claw['BY'] = claw['PY']

    # print(claw['PX']//claw['AX'], claw['PX']//claw['BX'])
    # print(claw['PY']//claw['AY'], claw['PY']//claw['BY'])
                # we have one winner
    # pass

