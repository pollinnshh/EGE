from itertools import *

alf = "0123456789"
count = 0
for val in product(alf, repeat=6):
    val = "".join(val)
    u1 = int(val) % 4 == 0
    u2 = len(val) == len(set(val))
    u3 = val[0] != "0"
    val1 = val.replace("2", "0").replace("4", "0").replace("6", "0").replace("8", "0")
    u4 = "00" not in val1
    if u1 and u2 and u3 and u4:
        count += 1
print(count)
