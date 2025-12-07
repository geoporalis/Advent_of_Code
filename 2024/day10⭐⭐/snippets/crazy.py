from pathlib import Path

example = True  #False  #

dir = Path(__file__).parent.resolve()

file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

area = { (x, y): c for y, l in enumerate(open(file).readlines()) 
                   for x, c in enumerate(l.strip()) }

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def find_trails(xy, trail):
    if area[xy] == '9':
        return [trail]
    else:
        trails = []
        for d in directions:
            n_xy = (xy[0] + d[0], xy[1] + d[1])
            if int(area.get(n_xy, 0)) - int(area.get(xy)) == 1:
                trails += find_trails(n_xy, trail + [n_xy])
        return trails

trailheads = [xy for xy in area if area[xy] == '0']

# count reachable peaks by counting unique last positions in trails
print("1:", sum(len(set(trail[-1] for trail in find_trails(xy, []))) 
                                  for xy in trailheads))
print("2:", sum(len(find_trails(xy, [])) for xy in trailheads))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# aoc = {complex(x,y):-1 if c=='.' else int(c)
#     for x,r in enumerate(open(filename)) for y,c in enumerate(r) if c>'\n'}

# def count(loc, height, seen):
#     if loc in aoc and height == aoc[loc]:
#         if height == 9: #and loc not in seen:
#             seen.add(loc)
#             return 1
#         return sum(count(loc+d, height+1, seen) for d in [1,-1,1j,-1j] if loc+d in aoc)
#     return 0

# print(sum(count(loc, 0, set()) for loc in aoc if aoc[loc]==0))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~