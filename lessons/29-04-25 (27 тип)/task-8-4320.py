from itertools import *

alf = "01234567"
cnt = 0
for val in product(alf, repeat=6):
    val = "".join(val)
    if val[0] != "0" and len(set(val)) == len(val) and (int(val, 8) % 5) == 0:
        val = val.replace("3", "1").replace("5", "1").replace("7", "1")
        val = val.replace("4", "2").replace("6", "2").replace("0", "2")
        if "11" not in val and "22" not in val:
            cnt += 1

print(cnt)
