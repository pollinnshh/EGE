from itertools import *

alf = "0123456789abcd"

cnt = 0
for val in product(alf, repeat=8):
    val = "".join(val)
    if val[0] != "0":
        if val.count("0") == 2:
            if sum([val.count(i) for i in "abcd"]) <= 4:
                cnt += 1

print(cnt)
