# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?

def perms(s):
    "Generate lexiographic permutations of s."
    assert(len(s) >= 1)

    if len(s) <= 1:
        yield s
    else:
        for i in range(len(s)):
            for p in perms(s[0:i] + s[i+1:]):
                yield s[i] + p

from itertools import islice

print next(islice(perms("0123456789"), 1000000 - 1, None))
