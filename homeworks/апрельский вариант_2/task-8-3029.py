from itertools import *

cnt = 0
alf = "012345678"
for val in product(alf, repeat=7):
    val = "".join(val)
    u1 = val[-1] not in "347"
    u2 = "000" not in val and "111" not in val and "222" not in val and "333" not in val and\
         "444" not in val and "555" not in val and "666" not in val and "777" not in val and\
         "888" not in val
    if val[0] != "0":
        if u1 and u2:
            cnt += 1

print(cnt)