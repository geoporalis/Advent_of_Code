from pathlib import Path

example = False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()


input = open(file).readlines()

curr = [0]*len(input[0])
curr[input[0].index('S')]=1

p1, p2 = 0, 1
for i in input[1:]:
    for col in range(len(curr)):
       if curr[col] > 0 and i[col] == '^':
          p1 += 1
          p2 += curr[col]
          curr[col-1] += curr[col]
          curr[col+1] += curr[col]
          curr[col] = 0

print(p1, p2)