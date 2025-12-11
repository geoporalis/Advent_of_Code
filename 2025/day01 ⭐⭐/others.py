from pathlib import Path

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() #if not example else Path(dir/'example').resolve()

# data = map(int, open(dir/'input').read().replace('L', '+').replace('R', '-').splitlines())
# cur, ans1, ans2 = 50, 0, 0
# for v in data:
#     ans2 += abs((cur-(v<0))//100 - (cur+v-(v<0))//100)
#     cur += v
#     ans1 += cur % 100 == 0
# print(ans1, ans2)

steps = map(int, open(dir/'input').read().replace('L', '+').replace('R', '-').splitlines())
pos, part_1, part_2 = 50, 0 ,0 

for step in steps:
    div, pos, prev = *divmod(pos + step, 100), pos
    part_1 += (pos == 0)
    part_2 += abs(div) - (prev == 0 and div < 0) + (pos == 0 and step < 0)
    
print(f"Part 1: {part_1}\nPart 2: {part_2}")