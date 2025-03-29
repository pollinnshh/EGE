from itertools import *

ans = []
for ch1 in "2468":
    for ch2 in "02468":
        for nech in "13579":
            for v1 in "0123456789":
                for v2 in "0123456789":
                    num = int(ch1 + "9" + v1 + "23" + v2 + "23" + nech + ch2)
                    if num % 1984 == 0:
                        ans.append([num, num // 1984])
ans = sorted(ans)
for i in ans:
    print(*i)
