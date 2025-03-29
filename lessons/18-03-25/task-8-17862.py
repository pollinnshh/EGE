from itertools import *

ans = []
for val in product("0123456789AB", repeat=5):
    val = "".join(val)
    u1 = val.count("9") + val.count("A") + val.count("B")
    if val[0] != "0":
        if val.count("7") == 1 and u1 <= 3:
            ans.append(val)
print(len(ans))