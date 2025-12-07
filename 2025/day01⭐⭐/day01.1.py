from pathlib import Path

example = False # True #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

dail=50
pasw =0
for l in open(file).readlines():
    l.strip('\n')
    num = int(l[1:])
    if l[0] == 'L': dail -= num 
    if l[0] == 'R': dail += num

    dail = dail % 100
    if dail < 0: dail += 100
    if dail == 0: pasw+=1 
    # print('dail: ',dail)

print(pasw)


# example:  3

# input:    1177

# crazy: 1502 # 1028136  ?manhatten distance?
