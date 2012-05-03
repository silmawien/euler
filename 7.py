# What is the 10 001st prime number?

from itertools import islice, count, ifilter
from math import sqrt

def is_prime(x):
    for d in range(2, int(sqrt(x) + 1)):
        if x % d == 0:
            return False
    return True

def nth(iterable, n):
    return next(islice(iterable, n, None))

primes = ifilter(is_prime, count(1))
print nth(primes, 10001)

