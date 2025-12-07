from pathlib import Path

example = True  #False # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

# dtat = [
dtat = {(x,y): c    for x, l in enumerate(open(file).readlines())
                    for y, c in enumerate(l)}

strt= [i for i in dtat if dtat[i]=='S'][0]
end = [i for i in dtat if dtat[i]=='E'][0]
wall= [i for i in dtat if dtat[i]=='#']
print(strt, end)
# dtat = [tuple(map(int , re.findall(r'-?\d+',l))) for l in open(file).readlines()]

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
fac = 0
def path(limit):
    seen = {*wall[:]}
    todo = [(0, strt, 0)]
    for d, (x,y), fac in todo:
        if (x,y) == end: return d
        for f, dd in (fac, 1), ((fac+1)&4, 1000), ((fac+3)&4, 1000):    # (x,y+1), (x,y-1), (x+1,y), (x-1,y):
            x,y = ( x + dirs[f][0], y + dirs[f][1])
            if (x,y) not in seen:
                todo.append((d+dd, (x,y), f))
                seen.add((x,y))

    return d

print(path(1024))  

# for x,y in (x,y+1), (x,y-1), (x+1,y), (x-1,y):

# for l in range(1024,len(dtat)):
#     if path(l) == 1e23:
#         print(l-1, dtat[l-1])
#         break