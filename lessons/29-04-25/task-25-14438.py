from itertools import *

ans = []
for p in range(1, 6):
    for v in "0123456789":
        for v2 in "0123456789":
            for num in product("0123456789", repeat=p):
                num = "".join(num)
                str = "17" + num + "46" + v + v2 + "8"
                if int(str) % 86513 == 0 and sum(map(int, str)) ** 0.5 == int(sum(map(int, str)) ** 0.5):
                    ans.append([int(str), int(str) // 86513])

ans = sorted(ans)
for i in ans:
    print(*i)
