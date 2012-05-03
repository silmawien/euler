# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) / gcd(a, b)

# lcm repeatedly should do the trick
print reduce(lcm, range(1, 21))

