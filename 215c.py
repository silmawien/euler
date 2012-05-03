# Fast dynamic attempt using cache

def compatible(row1, row2):
    return row1 & row2 == 0

# Now let's generate all possible rows of length n. There are
# about 3k of them, so we can brute force them quickly.

n, m = 32, 10

def allrows(n):
    rows = []

    for size in [2, 3]:
        if n - size > 0:
            for partial in allrows(n - size):
                partial += 1 << n - size
                rows.append(partial)
        elif n - size == 0:
            rows.append(0)

    return rows

# make a lookup table row -> [rows] from each possible row to
# a list of compatible rows
rs = allrows(n)
cache = {}
print "creating cache"
for r in rs:
    cache[r] = []
    for candidate in rs:
        if compatible(r, candidate):
            cache[r].append(candidate)
print "done"

# solve W(n, 1)
wn1 = {}
for row in allrows(n):
    wn1[row] = 1

# solve W(n, 2) by, for each possible row 1 r1, adding up the
# number of solutions for each row 2 compatible with this r1

current = wn1
for i in range(1, m):
    previous = current
    current = {}
    for row in allrows(n):
        c = 0
        for compat in cache[row]:
            c += previous[compat]

        current[row] = c

import operator as ops

print reduce(ops.add, [v for k, v in current.iteritems()], 0)

