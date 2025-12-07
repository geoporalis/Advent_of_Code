from colorama import Fore
from functools import cache
from pathlib import Path

example = False  # True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

pads = '789456123_0A<D>'
passcodes = [p for p in open(file).read().split('\n')]

# print(passcodes)
# for p in pads:
#     print(p, (pads.find(p)%3, pads.find(p)//3))

def getPath(path):  #von, nac
    (x, y), (X, Y) = [(pads.find(p)%3, pads.find(p)//3) for p in path]
    code = '>' * (X - x) + 'D' * (Y - y) + '0' * (y - Y) + '<' * (x - X)
    return code if (0,3) in [(x,Y), (X,y)] else code[::-1]

@cache
def recPath(passcode, recur):
    if recur < 0: return len(passcode)+1
    return sum(recPath(getPath(psc), recur-1) for psc in zip('A' + passcode, passcode + 'A'))

wieder = 25 # 2 #
score = 0
for passcode in passcodes:
    score += recPath(passcode[:3],wieder) * int(passcode[:3])

print('Answer:', score)
# input:    164684  # too high
#           154190  # too low

#crazy: 
# example : 126384
#           154115708116294
# input   : 157908
#           196910339808654


'''
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
'''