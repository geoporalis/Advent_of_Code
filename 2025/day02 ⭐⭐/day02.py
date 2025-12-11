from pathlib import Path
import math, re

example = False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

pasw1 = 0
pasw2 = 0
ranges = [r.split(',') for r in open(file).readlines() ][0]

pattern1 = re.compile(r'^(\d+)\1$')
pattern2 = re.compile(r'^(\d+)\1+$')

for r in ranges:
    begin, end = r.split('-')
    for x in range(int(begin), int(end)+1):
        # if pattern1.match(str(x)): pasw1 += x
        # if pattern2.match(str(x)): pasw2 += x

        xs = str(x)
        xl = len(xs)
        for d in range(1,(xl//2)+1):
            if (xl % d != 0): continue
            if xs == xs[:d]*(xl//d): 
                pasw2 += x
                break
        if (xl % 2 != 0): continue
        if xs[:xl//2] == xs[xl//2:]: pasw1 += x

sol1 = 1227775554 if example else 29940924880
sol2 = 4174379265 if example else 48631958998
print(pasw1, (pasw1 == sol1) , pasw1 - sol1)
print(pasw2, (pasw2 == sol2) , pasw2 - sol2)


# example:  1227775554

# input:    29940924880

