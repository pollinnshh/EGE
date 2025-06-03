from itertools import *

alf = "0123456789ABCDE"
cnt = 0
for val in product(alf, repeat=5):
    val = "".join(val)
    if val[0] != "0":
        if val.count("8") == 1 and len([i for i in val if i not in "0123456789"]) >= 2:
            cnt += 1

print(cnt)
