from pathlib import Path
from collections import defaultdict

example = False  #True  #

dir = Path(__file__).parent.resolve()

file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

checksum = 0

def levelUP(pebbles):
    new_pebbles = defaultdict(int)
    for stone, count in pebbles.items():
        ls = len(str(stone))
        if stone == 0:
            new_pebbles[1] += count
        elif ls % 2 == 0:
            s = str(stone)
            new_pebbles[int(s[0:(ls//2)])] += count
            new_pebbles[int(s[(ls//2):])] += count
        else:
            new_pebbles[int(stone)*2024] += count
    return new_pebbles

pebbles = {p : 1 for p in open(file).read().split()}
for i in range(25):
    pebbles = levelUP(pebbles)
checksum =  sum(pebbles.values())
print('Answer 1: ', checksum)

assert checksum == 55312 if example else 185894

pebbles = {p : 1 for p in open(file).read().split()}
for i in range(75):
    pebbles = levelUP(pebbles)
checksum =  sum(pebbles.values())

print('Answer 2: ', checksum)

assert checksum == 65601038650482 if example else 221632504974231

# example okay , input not ???

