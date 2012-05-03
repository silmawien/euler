# Faster, more idiomatic (?) version using memoization

n, m = 32, 10

def compatible(row1, row2):
    """Check if row1 may appear above/below row2"""
    return row1 & row2 == 0

def memoize(func):
    """Simple memoizing decorator."""
    cache = {}

    def apply(row):
        if row not in cache:
            cache[row] = func(row)
        return cache[row]

    return apply


@memoize
def allrows(n):
    """Generate all possible rows of length n"""
    rows = []

    for size in [2, 3]:
        if n - size > 0:
            for partial in allrows(n - size):
                partial += 1 << n - size
                rows.append(partial)
        elif n - size == 0:
            rows.append(0)

    return rows

@memoize
def allcompat(row):
    """Find all rows compatible with row."""
    return [c for c in allrows(n) if compatible(row, c)]

from itertools import repeat

# solve W(n, 1)
wn1 = dict(zip(allrows(n), repeat(1)))

# solve W(n, 2) by, for each possible row 1 r1, adding up the
# number of solutions for each row 2 compatible with this r1

current = wn1
for i in range(1, m):
    print "row %s" % i
    previous, current = current, {}
    for row in allrows(n):
        current[row] = sum([previous[c] for c in allcompat(row)])

print sum([v for k, v in current.iteritems()])

