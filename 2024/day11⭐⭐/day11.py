from colorama import Fore
from pathlib import Path

example = True  #False  #

dir = Path(__file__).parent.resolve()

file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

checksum = 0

stones = open(file).readlines()[0].strip()
# print(stones)
for blinks in range(75):
    pebbles = [s for s in stones.split(' ') if s != '']
    stones = ''
    # print(pebbles)
    # input()
    for pebble in pebbles:
        if pebble == '0':
            stones += ' 1'
        elif len(pebble) % 2 == 0:
            string1 = pebble[0:(len(pebble)//2)]
            string2 = pebble[(len(pebble)//2):].lstrip('0')
            if string2 == '':
                string2 ='0'
            stones += ' '+string1
            stones += ' '+string2
        else:
            stones += ' '+str(int(pebble)*2024)
    
    checksum = len(stones.split(' '))
    print('\r',blinks, checksum, end='  ')

checksum = len([s for s in stones.split(' ') if s != ''])


print('\nAnser: ', checksum) 
# print(stones)

# assert checksum == 55312 if example else 185894

# 185894 

# Rules:
'''
If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
'''