# Which starting number, under one million, produces the longest chain?

from eulertools import memoize

def lmemo(m):
    """A memoizer for 1 int-param that won't cache values > m."""
    def decorator(f):
        cache = {}
        def apply(n):
            if n < m:
                if n not in cache:
                    cache[n] = f(n)
                return cache[n]
            else:
                return f(n)
        return apply
    return decorator

@lmemo(1000000)
def seqlen(n):
    """Find the length of the sequence starting at n."""
    if n <= 1:
        return 1
    elif n % 2 == 0:
        return 1 + seqlen(n / 2)
    else:
        return 1 + seqlen(3 * n + 1)

print max([(s, seqlen(s)) for s in range(1, 1000000)], key=lambda x: x[1])

