from itertools import *

alf = sorted("лунатик")
for pos, val in enumerate(product(alf, repeat=6), 1):
    val = "".join(val)
    u1 = val.count("а") + val.count("и") + val.count("у") == 1
    if u1 and val[0] == "н":
        print(pos, val)
