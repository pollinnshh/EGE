from itertools import *

cnt = 0
alf = "012345678"
for val in product(alf, repeat=7):
    val = "".join(val)
    if val[0] != "0":
        if val[0] not in "1357":
            if val.count("6") >= 1 and val[-1] not in "036":
                cnt += 1

print(cnt)
