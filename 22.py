# What is the total of all the name scores in the file?

# file is structured like "NAME1","NAME2",...
with open("names.txt") as f:
    names = (s.strip('"') for s in f.read().split(','))

def avalue(s):
    "Sum of character values, A=1, B=2, etc."
    return sum(ord(c) - ord("A") + 1 for c in s)

print sum(avalue(s) * i for (i, s) in enumerate(sorted(names), 1))

