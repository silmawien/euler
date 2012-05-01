# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# find the least factor of n
# return factor f and remainer n/f or None if no factors exist
def factor(n):
    #  xrange won't do large integers, at least not in python 2.x
    f = 2
    while f < n:
        if n % f == 0:
            return (f, n/f)
        f += 1
    return None

n = 600851475143
while factor(n):
    f, n = factor(n)

print n

