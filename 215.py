# Note: The below brute force solution was too slow. See 215b.py.

# There are eight ways of forming a crack-free 9x3 wall, written W(9,3) = 8.
# Calculate W(32,10).

n, m = 9, 2

# initial position
# 0 represents top left, before the first block
# n*m is bottom right, just past the last block
pos = 0

# W(n, m) data structure: dict, where keys are positions
# and any value represents a crack in that position
wall = {}

# the wall starts off with cracks running down each side
for i in range(0, n*m+1):
    if i % n == 0:
        wall[i] = True

# helper to check if we can put a block in a certain position
def validblock(wall, pos, size):
    column = pos % n
    fitsOnRow = column + size <= n
    crackBeneath = (pos + size - n) in wall
    atEdge = (pos + size) % n == 0
    #print "fits %s crack %s atEdge %s" % (fitsOnRow, crackBeneath, atEdge)
    return fitsOnRow and (not crackBeneath or atEdge)


def numsolutions(wall, pos):
    # are we done?
    if pos == n*m:
        return 1

    # are we past the end ?
    if pos > n*m:
        return 0

    result = 0

    # try adding each type of block and recurse
    for size in [2, 3]:
        #print "trying %s brick at %s in %s" % (size, pos, wall)
        if validblock(wall, pos, size):
            #print "valid"
            wall[pos + size] = True
            result += numsolutions(wall, pos + size)
            del(wall[pos + size])

    return result


print numsolutions(wall, pos)

