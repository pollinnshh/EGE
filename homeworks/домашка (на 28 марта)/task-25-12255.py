from itertools import *

ans = []
for p in range(3):
    for z in product("0123456789", repeat=p):
        for v1 in "0123456789":
            for v2 in "0123456789":
                for v3 in "0123456789":
                    z = "".join(z)
                    num = "12" + v1 + "3" + z + "456" + v2 + v3 + "9"
                    if int(num) % 98591 == 0:
                        ans.append([int(num), int(num) // 98591])

for i in sorted(ans):
    print(*i)
