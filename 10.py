# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# The first 2 million integers fits in memory. Generate the complete list and
# zero out the non-prime indices using a sieve.
def sieve(n):
    ps = list(range(0, n))
    ps[0] = 0
    ps[1] = 0
    i = 2
    while i < n / 2:
        if ps[i] != 0:
            for j in range(2 * i, n, i):
                ps[j] = 0
        i += 1

    return ps

print sum(sieve(2000000))

