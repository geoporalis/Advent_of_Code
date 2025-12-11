l=[1,2,3,4,4,5,5,6]
l.remove(4)
print(l)

# from itertools import chain, groupby

# r = range(2,7)
# s = range(4,10)
# t = range(5,12)

# u = [r ,s ,t]

# v = set().union(w for w in u)

# print(v)
# w = chain(r,s,t)
# y = set()

# y |= (set(z) for z in w)

# def ranges(i):
#     for a, b in groupby(enumerate(i), lambda pair: pair[1] - pair[0]):
#         b = list(b)
#         yield range(b[0][1], b[-1][1])

# print(list(ranges([0, 1, 2, 3, 4, 7, 8, 9, 11])))
# print(list(ranges(w)))

# # r.extend(range(0))
# for x in w: print (x)
# print(set(r) | set(s) | set(t) )
# print(5 in w, 4 in w)

# print(r[0], r[-1])


