from itertools import *

ans = []
for r in range(6):
    for z in product("2468", repeat=r):
        z = "".join(z)
        for v1 in "13579":
            for v2 in "13579":
                num = int(z + "12" + v1 + "4" + v2)
                if num % 9231 == 0:
                    ans.append([num, num // 9231])
ans = sorted(ans)
for i in ans:
    print(*i)