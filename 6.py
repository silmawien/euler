# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

sumsquares = sum([n * n for n in range(1, 101)])
squaresum = sum(range(1, 101)) ** 2

print sumsquares - squaresum
