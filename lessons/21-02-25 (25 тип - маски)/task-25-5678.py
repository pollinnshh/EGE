from itertools import *

ans = []
for r1 in range(3):
    for r2 in range(3 - r1):
        for z1 in product("0123456789", repeat=r1):
            for z2 in product("0123456789", repeat=r2):
                z1 = "".join(z1)
                z2 = "".join(z2)
                num = "124" + z1 + "5" + z2 + "79"
                summ = sum([int(i) for i in num if int(i) % 2 != 0])
                if int(num) % summ == 0:
                    ans.append([int(num), sum(map(int, num))])
ans = sorted(ans)
for i in ans:
    print(*i)