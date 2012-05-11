# Find the maximum total from top to bottom of the triangle ...

with open("triangle.txt") as f:
    lines = f.readlines()

t = [map(int, line.split()) for line in lines]

from eulertools import memoize

def maxpath(t):
    "Maximum total path through triangle t starting from top"

    @memoize
    def path(x, y):
        if y == len(t):
            return 0
        else:
            return t[y][x] + max([path(x, y + 1), path(x + 1, y + 1)])

    return path(0, 0)

print maxpath(t)
