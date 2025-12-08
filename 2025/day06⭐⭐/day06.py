from pathlib import Path
import math

example = False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()
numbers = open(file).read().split('\n')
idxNsigns = [[i,c] for i,c in enumerate(numbers[-1]) if c in '+*']
idxNsigns.append([len(numbers[0]), '#'])

part1=0
for i, s in enumerate(idxNsigns[:-1]):
    start, sign, end = (s[0], s[1], idxNsigns[i+1][0])
    nums = [int(n[start:end]) for n in numbers[:-1]]
    part1 += sum(nums) if sign == '+' else math.prod(nums)

part2=0
nums = []
for i in range(len(numbers[0])-1,-1,-1):
    nus = ''.join(n[i] for n in numbers[:-1]).strip()
    if nus != '': nums.append(int(nus))

    if numbers[-1][i] in '+*':
        part2 += sum(nums) if numbers[-1][i] == '+' else math.prod(nums)
        nums=[]

sol1 = 4277556 if example else 5316572080628
print(part1, (part1 == sol1) , part1 - sol1)
sol2 = 3263827 if example else 11299263623062
print(part2, (part2 == sol2) , part2 - sol2)  