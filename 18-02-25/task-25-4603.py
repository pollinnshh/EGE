## 1 способ
from itertools import *

ans = []
for r in range(4):
    for z in product("0123456789", repeat=r):
        z = "".join(z)

        num = int("1234" + z + "7")
        if num % 141 == 0:
            ans.append([num, num // 141])

ans = sorted(ans)
for i in ans:
    print(*i)

## 2 способ
from fnmatch import fnmatch

for i in range(12347 - 12347 % 141, 10**8, 141):
    if fnmatch(str(i), "1234*7"):
        if i % 141 == 0:
            print(i, i // 141)