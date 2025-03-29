from itertools import *

alf = sorted("калейдосп")[::-1]
for pos, val in enumerate(product(alf, repeat=6), 0):
    val = "".join(val)
    if pos % 2 == 0 and val[0] == "к" and val.count("й") >= 2 and val.count("с") == 0 and val.count("е") == 0:
        print(pos, val)