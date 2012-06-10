# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.

def cyclelen(d):
    "Find the length of the longest recurring cycle of digits in 1/d"
    seen = {} # state -> pos
    n = 1
    pos = 0
    while n != 0:
        while n < d:
            n *= 10
        if (n, d) in seen:
            return pos - seen[(n, d)]
        seen[(n, d)] = pos
        (q, n) = divmod(n, d)
        pos += 1

    return 0

print max(((n, cyclelen(n)) for n in range(1, 1000)), key=lambda x: x[1])

