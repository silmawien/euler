# Your task has been made easy, as the encryption key consists of three lower
# case characters. Using cipher1.txt (right click and 'Save Link/Target
# As...'), a file containing the encrypted ASCII codes, and the knowledge that
# the plain text must contain common English words, decrypt the message and
# find the sum of the ASCII values in the original text.
from collections import defaultdict
import itertools
import operator
import re

with open("/usr/share/dict/words") as f:
    words = set([w.strip() for w in f.readlines()])

with open("cipher1.txt") as f:
    cipher = eval("[" + f.read().strip() + "]")

def decode(cipher, key):
    return ''.join([chr(c ^ key[i % len(key)]) for i, c in enumerate(cipher)])

def guess(key):
    "Check if key produces a legible cleartext."
    decoded_words = re.split(r'\W+', decode(cipher[0:60], key))
    # check for a reasonable frequency of 2+ letter words
    longwords = [w for w in decoded_words if w.lower() in words and len(w) > 1]
    if len(longwords) / float(len(decoded_words)) > 0.5:
        print key, longwords[0:5], sum(ord(c) for c in decode(cipher, key))

# We could brute force all 26^3 combinations, but let's try something more
# efficient.

# calculate cipher letter frequencies
d = defaultdict(int)
for x in cipher:
    d[x] += 1

cipher_freqs = sorted(d.iteritems(), key=operator.itemgetter(1))

# The frequencies will be roughly 1/3 of what we expect, since an input "e" is
# XORed with each of the three key values with equal probability. In addition,
# the same output can result from several input letters, XORed by different
# values.  For long keys this should make frequency analysis useless. This key
# is very short though, so let's guess part of it.

common_letters = "etai "
for c in common_letters:
    # check that most common 10 outputs
    for i in range(-1, -10, -1):
        # assume that c produced this letter
        g = cipher_freqs[i][0] ^ ord(c)
        print "Testing '%s' = '%s'" % (c, cipher_freqs[i][0])
        # brute force the other two key letters
        for a in range(ord('a'), ord('z') + 1):
            for b in range(ord('a'), ord('z') + 1):
                guess([g, a, b])
                guess([a, g, b])
                guess([a, b, g])

