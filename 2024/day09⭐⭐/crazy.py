from pathlib import Path

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() 

# D = [(i//2+1 if i%2 else 0, int(d)) for i,d in
#         enumerate(open(file).read(), 1)]

# for i in range(len(D))[::-1]:
#     for j in range(i):
#         i_data, i_size = D[i]
#         j_data, j_size = D[j]

#         if i_data and not j_data and i_size <= j_size:
#             D[i] = (0, i_size)
#             D[j] = (0, j_size - i_size)
#             D.insert(j, (i_data, i_size))


# flatten = lambda x: [x for x in x for x in x]

# print(sum(i*(c-1) for i,c in enumerate(flatten(
#     [d]*s for d,s in D)) if c))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## This is significantly cleaned up and rewritten version of Part 2 from what I initially used to get my star. For that initial implementation, I used a single list or tuples with id, start position, and length, where an id of None indicated a free space. I worked from right to left keeping the list ordered, using a set to indicate files that had already been moved, and did a pass to coalesce and free blocks.

## While experimenting with cleaning it up, I realized that it would be more efficient to split out the files from the free space into separate list. Then the file id is implicit in the list index, and I no longer need a set to indicate if it's been moved -- I just iterate them in reverse. Likewise, I realized there's no need to coalesce free space since files only move left. And it's okay to leave free space that's now zero-length. So the code got a lot simpler and faster.

# f, s, p = [], [], 0
# for i, l in enumerate( map( int, open( file ).read().strip() ) ):
#     ( f, s )[ i % 2 ].append( ( p, l ) )
#     p += l

# for fi in range( len( f ) - 1, -1, -1 ):
#     fp, fl = f[ fi ]
#     for si, ( sp, sl ) in enumerate( s ):
#         if sl >= fl:
#             f[ fi ] = ( sp, fl )
#             s[ si ] = ( sp + fl, sl - fl )
#             break
#         if sp >= fp:
#             break

# print( sum( sum( n * x for x in range( p, p + l ) )
#             for n, ( p, l ) in enumerate( f ) ) )
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# from collections import defaultdict
# import heapq

# with open(file) as f:
#     rawinput = f.read()

# lengths = [int(num) for num in rawinput]

# filled_grid = {} # ID: start,length
# gaps = defaultdict(lambda: []) # length: start

# cur_pos = 0
# for i,num in enumerate(lengths):
#     if i%2 == 0:
#         filled_grid[i//2] = [cur_pos,num]
#     else:
#         if num > 0:
#             heapq.heappush(gaps[num],cur_pos)
#     cur_pos += num

# for i in sorted(filled_grid.keys(),reverse=True):
#     file_start_pos,file_len = filled_grid[i]
#     possible_gaps = sorted([[gaps[gap_len][0],gap_len] for gap_len in gaps if gap_len>=file_len])
#     if possible_gaps:
#         gap_start_pos,gap_len = possible_gaps[0]
#         if file_start_pos > gap_start_pos:
#             filled_grid[i] = [gap_start_pos,file_len]
#             remaining_gap_len = gap_len-file_len
#             heapq.heappop(gaps[gap_len])
#             if not gaps[gap_len]:
#                 del gaps[gap_len]
#             if remaining_gap_len:
#                 heapq.heappush(gaps[remaining_gap_len],gap_start_pos+file_len)
                
# answer = sum(num*(start*length+(length*(length-1))//2) for num,(start,length) in filled_grid.items()) # (start) + (start+1) + ... + (start+length-1)
# print(answer)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

used = []
p2 = []

data = open( file ).read().strip()

for i, ch in enumerate(data):
  if i % 2 == 0:
    used.extend([i//2]*int(ch))
    p2.append((i//2, int(ch)))
  else:
    used.extend([None]*int(ch))
    p2.append((None, int(ch)))

def move_blks():
  disk = used[:]
  for i in range(len(disk)-1, -1, -1):
    if disk[i] is None:
      continue
    for j in range(i):
      if disk[j] is None:
        disk[j], disk[i] = disk[i], None
        break
  return disk


def part1():
  disk = move_blks()
  tot = 0
  for i, fid in enumerate(disk):
    if fid is not None:
      tot += i * fid
  return tot

def move_files():
  disk = p2[:]
  last_fid, _ = disk[-1]
  for fid in range(last_fid, -1, -1):
    for i in range(len(disk)):
      t_fid, flen = disk[i]
      if t_fid == fid:
        break

    # insert
    for j in range(i):
      jfid, empty_blocks = disk[j]
      if jfid is not None:
        continue
      if flen <= empty_blocks:
        remain = empty_blocks - flen
        disk[j] = disk[i]
        disk[i] = (None, flen)
        if remain:
          disk = disk[:j+1] + [(None, remain)] + disk[j+1:]
        break

  return disk

def expand_disk(disk):
  full = []
  for fid, flen in disk:
    full.extend([fid]*flen)
  return full

def pprint(disk):
  d = disk[:]
  for i in range(len(d)):
    if d[i] is None:
      d[i] = '.'
  print(''.join(map(str, d)))


def part2():
  disk = expand_disk(move_files())
  tot = 0
  for i, fid in enumerate(disk):
    if fid is not None:
      tot += i * fid
  return tot

print(part1())
print(part2())