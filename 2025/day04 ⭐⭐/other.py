# grid = [l.strip() for l in open('input')]
# grid = {(r,c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '@'}
# neigh = lambda r,c: sum((r+dr,c+dc) in grid for dr in [-1,0,1] for dc in [-1,0,1] if dr or dc)
# avail = lambda: {(r,c) for r,c in grid if neigh(r,c) < 4}
# print(len(avail()))
# total = len(grid)
# while len(avail()): grid -= avail()
# print(total - len(grid))


# data = [l.strip() for l in open('input')]
# grid = {(r, c) for r in range(len(data)) for c in range(len(data[0])) if data[r][c] == '@'}
# dirs = {(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)}

# P1 = 0
# for r, c in grid: 
#     if sum(1 for dr, dc in dirs if (r + dr, c + dc) in grid) < 4: P1 += 1
# print(P1)

# P2 = set()
# while True:
#     for r, c in grid:
#         if sum(1 for dr, dc in dirs if (r + dr, c + dc) in grid) < 4: P2.add((r,c))
#     if not grid & P2: break
#     grid -= P2
# print(len(P2))


paper = {i + 1j * j for i, line in enumerate(open('input').read().split()) for j, c in enumerate(line) if c == "@"}
octdir, removed = ({1, 1j, -1, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j}, [])

while to_remove := {z for z in paper if len({z + dz for dz in octdir} & paper) < 4}:
    removed.append(len(to_remove))
    paper -= to_remove

# Part 1
print(removed[0])

# Part 2
print(sum(removed))