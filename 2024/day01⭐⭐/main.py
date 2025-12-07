from pathlib import Path 

dir = Path(__file__).resolve().parents[0]

leftlist = []
rightlist = []

with open(Path(dir/'input').resolve() , 'r') as f:
    for x in f.readlines():
        le, re = x.strip().split('  ')
        leftlist.append(int(le))
        rightlist.append(int(re))

leftlist_sorted = sorted(leftlist)
rightlist_sorted = sorted(rightlist)

distance = 0

for idx in range(len(leftlist_sorted)):
    distance += abs(leftlist_sorted[idx] - rightlist_sorted[idx])

print(distance)

similarity = 0

for element in leftlist_sorted:
    similarity += element*sum(1 for p in rightlist_sorted if p == element)

print(similarity)