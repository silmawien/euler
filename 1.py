# find the sum of all natural numbers less than 1000 that are are multiples
# of 3 or 5

def is_cool(n):
    return n % 3 == 0 or n % 5 == 0

numbers = [ n for n in range(1, 1000) if is_cool(n) ]
# oops i misread sum as product
# leaving this in as proof of python's awesomeness
# product = sum(lambda x, y: x * y, numbers, 1)
print sum(numbers)
