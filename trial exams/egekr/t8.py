from itertools import *

alf = sorted("победа")
for pos, val in enumerate(product(alf, repeat=6), 1):
    val = "".join(val)
    if pos % 2 == 0:
        if val[0] == "о" and len(val) == len(set(val)):
            print(pos, val)
