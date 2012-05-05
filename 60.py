# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.

from itertools import islice, count, ifilter, combinations
from math import sqrt
from eulertools import memoize
import psyco

# Reduces run time by about 4/5
psyco.full()

# Brute force search all combinations of the first <limit> primes
# The guess has to be quite good, or the O(n^5) complexity eats our lunch.
limit = 1500

def is_prime(x):
    lim = int(sqrt(x)) + 1
    for d in xrange(2, lim):
        if x % d == 0:
            return False
    return True

# get the list of candidate primes
ps = list(islice(ifilter(is_prime, count(2)), limit))

# match function (memoizing this cuts runtime by ~ 1/2)
@memoize
def m(p1, p2):
    s1 = int(str(p1) + str(p2))
    s2 = int(str(p2) + str(p1))
    return is_prime(s1) and is_prime(s2)

# O(n^5) search with no pruning - compact but too slow
def slowsearch(ps):
    for candidates in combinations(ps, 5):
        if all((m(a, b) for (a, b) in combinations(candidates, 2))):
            print "%s, sum = %s" % (items, sum(items))
            exit()

# a version that prunes whole subtrees when a match fails
def search(first, items):
    if len(items) == 5:
        print "%s, sum = %s" % (items, sum(items))
        exit()

    for i in range(first, len(ps)):
        e = ps[i]
        if not all((m(e, x) for x in items)):
            continue
        search(i + 1, items + (e,))

# this runs in ~30 seconds on a VIA C7 1GHz
#slowsearch(ps)
search(0, ())

