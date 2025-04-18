from itertools import *

cnt = 0
alf = sorted(set("инставка"))
for val in product(alf, repeat=4):
    val = "".join(val)
    if val[0] in "тнсвк" and val[-1] in "иа":
        cnt += 1
        if val == "ника":
            print(cnt)
