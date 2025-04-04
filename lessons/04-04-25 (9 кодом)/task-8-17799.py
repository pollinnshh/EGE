from itertools import *

alf = sorted("аргумент")
for pos, val in enumerate(product(alf, repeat=4), 1):
    val = "".join(val)
    if len(set(val)) == len(val) and "".join(sorted(val)) == val:
        print(pos, val)
