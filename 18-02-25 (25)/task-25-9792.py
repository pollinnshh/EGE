from itertools import *

ans = []
for r in range(3):
    for z in product("0123456789", repeat=r):
        for v1 in "0123456789":
            for v2 in "0123456789":
                z = "".join(z)

                num = int("1" + z + "2" + v1 + v2 + "76")
                if num % 1923 == 0:
                    ans.append([num, num // 1923])
ans = sorted(ans)
for i in ans:
    print(*i)