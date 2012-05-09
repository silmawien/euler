# What is the value of the first triangle number to have over five hundred
# divisors?

from eulertools import memoize
from collections import defaultdict
from itertools import chain
import operator as op

# The nth triangle number T(n) = n * (n + 1) / 2
# Factor n and n+1 separately to avoid factoring large numbers.
# Count number of unique ways to combine factors.

from math import sqrt

def factors(n):
    "Break n into a list of prime factors. 28 -> [2, 2, 2, 7]."
    c = 2
    while c * c <= n and n % c != 0:
        c += 1
    if c * c <= n:
        return [c] + factors(n / c)
    else:
        return [n]

# find number of unique combinations of factors from T(n)
def combos(n):
    # Create a histogram of factors.
    # Start at 2 since n instances of a factor increase combinations by *n+1
    cs = defaultdict(lambda: 1)
    # n * n+1
    for x in factors(n):
        cs[x] += 1
    for x in factors(n + 1):
        cs[x] += 1
    # / 2
    cs[2] -= 1
    return reduce(op.mul, cs.itervalues(), 1)

M = 0
n = 0
c = 0
while c < 500:
    n += 1
    c = combos(n)
    if c > M:
        M = c
        print M, n, n*(n+1)/2

