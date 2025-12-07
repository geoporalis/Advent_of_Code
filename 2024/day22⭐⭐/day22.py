from colorama import Fore
from functools import cache
import json
import sys
sys.setrecursionlimit(2100)

from pathlib import Path

example = False  # True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

prices = [int(p) for p in open(file).read().split('\n')]

def mix(secret, new):   #bitwise xor
    return secret ^ new

def prune(secret):
    return secret % 16777216

def times64(secret):
    return prune(mix(secret*64, secret))

def divide32(secret):
    return prune(mix(secret//32, secret))

def times2048(secret):
    return prune(mix(secret*2048, secret))

def calcNewSecret(price):
    return times2048(divide32(times64(price)))

@cache
def calc2000(price, rec):
    if rec == 0: return price
    return calc2000(
        calcNewSecret(price), 
        rec-1)

secretSequence = {}
def calcAll(price):
    seq = []
    sequences = {}
    d=2000
    while (d > 0):
        last_one = int(str(price)[-1])
        d-=1
        price = calcNewSecret(price)
        new_one = int(str(price)[-1])
        seq.append(str(new_one - last_one))
        if len(seq) > 4: seq.pop(0)
        if len(seq) == 4:
            seqs = ','.join(seq)
            if not seqs in sequences: sequences[seqs] = new_one
        last_one = new_one

    for key, val in sequences.items():
        if key in secretSequence: secretSequence[key] += val
        else: secretSequence[key] = val
    
    return price

print(sum(calcAll(price) for price in prices))

maxbanans = 0
for key, val in secretSequence.items():
    maxbanans = maxbanans if maxbanans > val else val

print(maxbanans)

# price=123
# for i in range(10):
#     price = times2048(divide32(times64(price)))
#     print(price)

# example:  37327623 # 
# input:    15608699004 # spot on
# part2:    1948 # too high     only 1st occurence!!!!
#           1791