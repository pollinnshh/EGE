from itertools import *
alf = sorted("школа")
for pos, val in enumerate(product(alf, repeat=5),1):
    val = "".join(val)
    if val == "шалаш":
        print(pos)