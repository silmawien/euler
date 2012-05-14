# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

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

M = 28123

abundants = set()
result = 0
for n in range(1, M):
    if sum(divisors(n)) > n:
        abundants.add(n)
    if not any(n - a in abundants for a in abundants):
        result += n

print result

