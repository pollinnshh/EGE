from itertools import *

alf = "01234567"
cnt = 0
for val in product(alf, repeat=5):
    val = "".join(val)
    if val[0] != "0":
        if val.count("1") == 0 and len(val) == len(set(val)):
            val = val.replace("2", "0").replace("4", "0").replace("6", "0")
            val = val.replace("3", "1").replace("5", "1").replace("7", "1")
            if "11" not in val and "00" not in val:
                cnt += 1

print(cnt)