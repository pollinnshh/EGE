from itertools import *

alf = sorted("марксл")
for num, val in enumerate(product(alf, repeat=6), 1):
    val = "".join(val)
    list = [val.count(i) for i in val]
    if "кс" not in val and "ск" not in val and list.count(3) == 3 and list.count(1) == 3:
        print(num, val)
