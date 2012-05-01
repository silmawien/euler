# find the sum of all even fibonacci numbers <= 4000000

from itertools import takewhile

# was going for a loop first, but
# decided to try generators instead
#def fib(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return fib(n - 2) + fib(n - 1)

def fibgen():
    a = 0
    b = 1
    yield 0
    while True:
        yield b
        a, b = b, a + b

somefibs = takewhile(lambda x: x <= 4000000, fibgen())
evenfibs = [n for n in somefibs if n % 2 == 0]
print sum(evenfibs)

