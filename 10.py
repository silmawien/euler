# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1, 1000 / 2):
    rest = 1000 - a
    for b in range(a + 1, rest - a):
        c = rest - b;
        if a * a + b * b == c * c:
            print (a, b, c), a*b*c
            exit()

