# A dynamic attempt, since brute forcing didn't work.

# A row is represented by a bit set of crack positions
# from 1 to n - 1. Cracks at the edges 0 and n are implied,
# and not in the set. For example, the row of length 5 that
# has a 2-brick and a 3-brick is represented as {2} or 1 << 2 = 4.

# We might want to pretty-print rows, so let's start with that.
def printrow(n, row):
    s = ""
    for i in range(0, n):
        if i == 0 or (row >> i) & 1 == 1:
            s += "|"
        else:
            s += " "
        s += "-"
    s += "|"
    print s

# Let's enable string -> row conversion
def makerow(s):
    row = 0
    for i, c in enumerate(s):
        if c == "|" and i > 0 and i < len(s) - 1:
            row += 1 << (i / 2)
    return row

print makerow("|- - -|- -|")
printrow(5, makerow("|- - -|- -|"))

# Testing if two rows are 'compatible', i.e. if one can go
# above the other, is just bitwise and.

def compatible(row1, row2):
    return row1 & row2 == 0

print compatible(makerow("|- - -|- -|"), makerow("|- -|- - -|"))
print compatible(makerow("|- - -|- -|"), makerow("|- - -|- -|"))

# Now let's generate all possible rows of length n. There are
# about 3k of them, so we can brute force them quickly.

n = 32

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

print len(allrows(n))

# Incidentally this is the answer for W(n, 1).

# Ok now for the algorithm. We are going to build the answer row by row,
# in dynamic fashion.

# For W(n, 1) there is obviously 1 solution for each item in allrows(n),
# so let's store that as a result array. The reason will be clear shortly.

wn1 = []
for row in allrows(n):
    wn1.append((row, 1))

# To get W(n, 2) we again look at each possibility for the bottom row.
# For each one, we find all compatible rows in wn1 and sum them up.

# We can go on building the next row in the same manner, all the way to
# row m

m = 10

print "m:"
current = wn1
for i in range(1, m):
    previous = current
    current = []
    for row in allrows(n):
        c = 0
        for prow, pc in previous:
            if compatible(prow, row):
                c += pc

        current.append((row, c))
    print "iteration %s complete" % i

import operator as ops

print "grand total:"
print reduce(ops.add, [c for (row, c) in current], 0)

# This really got my Via C7 working for a few minutes. One way to speed it
# up would be to cache lists of compatible rows, so that the inner loop
# only has to iterate over working combinations. Lots of tips on the forum.

