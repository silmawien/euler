# Evaluate the sum of all the amicable numbers under 10000.
from collections import defaultdict

def divisors(n):
    "Generate a list of proper divisors of n"
    assert(n >= 1)
    yield 1
    c = 2
    while c * c < n:
        if n % c == 0:
            yield c
            yield n / c
        c += 1
    if c * c == n:
        yield c

d = defaultdict(int, [(n, sum(divisors(n))) for n in range(1, 10000)])
amicables = [n for n in d.keys() if d[n] != n and d[d[n]] == n]
print sum(amicables)
