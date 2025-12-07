from colorama import Fore
from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()

file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

checksum = 0


# my solution would work i guess but takes too long
# def checkBlinks(blinks):
#     return True if len([b for b in blinks if len(b)>0]) > 0 else False

# def checkPebble(pebble):
#     if pebble == '0':
#         return ['1']
#     if len(pebble) % 2 == 0:
#         string1 = pebble[0:(len(pebble)//2)]
#         string2 = pebble[(len(pebble)//2):].lstrip('0')
#         if string2 == '':
#             string2 ='0'
#         return [string1,string2]
#         # return string1, string2
    
#     return [str(int(pebble)*2024)]

# number_of_blicks = 74 # 24   # 
# blinks = [[]]*(number_of_blicks+1)
# blinks[0] = open(file).readlines()[0].strip().split(' ')

# while checkBlinks(blinks):
#     for level in reversed(range(len(blinks))):
#         if len(blinks[level]) == 0:
#             continue
#         pebble = blinks[level].pop(0)
#         pebble = checkPebble(pebble)
#         if level == number_of_blicks:
#             checksum += len(pebble)
#         else:
#             blinks[level+1] = pebble
#         break
#     print('\r',checksum, end='')

# lets play with some hints work:
from functools import cache

# pebbles = map(int, open(file).read().split())
pebbles = [p for p in open(file).read().split()]

@cache
def countPebbles(pebble, level=25):
    if level == 0:  return 1
    if pebble == 0: return countPebbles(1, level-1)
    ps = str(pebble)
    pl = len(ps)
    if pl & 1 == 0:
        return ( countPebbles(int(ps[0:(pl//2)]), level-1) +
                 countPebbles(int(ps[(pl//2):]), level-1) )
    
    return countPebbles(pebble*2024, level-1)


for p in pebbles:
    checksum += countPebbles( int(p), 25)

print('\rAnser1: ', checksum) 

assert checksum == 55312 if example else 185894

checksum = 0
for p in pebbles:
    checksum += countPebbles( int(p), 75)

print('\rAnser2: ', checksum) 

assert checksum == 65601038650482 if example else 221632504974231

# 221632504974231

# checksum = sum(countPebbles( p , 25) for p in pebbles)

# checksum = sum( countPebbles( p, 25 ) for p in pebbles )
# checksum = sum( map(countPebbles, pebbles ))


