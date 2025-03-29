## 1
from itertools import *

ans = []
for r in range(3):
    for z in product("0123456789", repeat=r):
        for v in range(10):
            z = "".join(z)

            num = int("12" + z + "4" + str(v) + "65")
            if num % 161 == 0:
                ans.append([num, num // 161])

ans = sorted(ans)
for i in ans:
    print(*i)

## 2
from fnmatch import *

for i in range(161, 10**8, 161):
    if fnmatch(str(i), "12*4?65"):
        if i % 161 == 0:
            print(i, i // 161)