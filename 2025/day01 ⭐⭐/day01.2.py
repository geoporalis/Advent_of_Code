from pathlib import Path

example = False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

dail=50
pasw1 =0
pasw2 =0
for l in open(file).readlines():
    l.strip('\n')
    dist = int(l[1:])
    for i in range(1,dist+1):
        dail+= 1 if l[0] == 'R' else -1
        if l[0] == 'L' and dail < 0: dail = 99
        if l[0] == 'R' and dail > 99: dail = 0
        if dail == 0: pasw2+=1

    if dail == 0: pasw1+=1
    # print('dail: ',dail)

print(pasw1, pasw2)


# example:  6

# input:    2702 # 3879 # 7499

# crazy: 1502 # 1028136  ?manhatten distance?
