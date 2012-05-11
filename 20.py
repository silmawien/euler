import operator as op
fac100 = reduce(op.mul, range(1, 101))
print sum(map(int, str(fac100)))

