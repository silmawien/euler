# What is the first term in the Fibonacci sequence to contain 1000 digits?
from eulertools import memoize

@memoize
def fib(n):
    return 1 if n == 1 or n == 2 else fib(n - 1) + fib(n - 2)

n = 1
while (len(str(fib(n))) < 1000):
    n +=1
print n
