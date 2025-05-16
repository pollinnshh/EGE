from itertools import *

cnt = 0
alf = "0123456789"
for n in product(alf, repeat=5):
    n = "".join(n)
    if n[0] != "0":
        if n[-1] not in "347":
            if "000" not in n and "111" not in n and "222" not in n and "333" not in n and "444" not in n and \
                    "555" not in n and "666" not in n and "777" not in n and "888" not in n and "999" not in n:
                cnt += 1

print(cnt)