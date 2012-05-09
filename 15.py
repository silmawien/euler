# coding=UTF-8
# How many routes are there through a 20×20 grid?

from eulertools import memoize

@memoize
def paths(x, y):
    if x == 0 or y == 0:
        return 1
    else:
        return paths(x - 1, y) + paths(x, y - 1)

print paths(20, 20)

