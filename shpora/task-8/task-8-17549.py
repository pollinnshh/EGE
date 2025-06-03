from itertools import *

alf = sorted("фокус")
for pos, val in enumerate(product(alf, repeat=5), 1):
    val = "".join(val)
    if val.count("ф") == 0 and val.count("у") == 2:
        print(pos)
