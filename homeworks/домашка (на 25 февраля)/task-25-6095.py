from itertools import *

ans = []
for r1 in range(3):
    for r2 in range(3 - r1):
        for z1 in product("123456789", repeat=r1):
            for z2 in product("0123456789", repeat=r2):
                z1 = "".join(z1)
                z2 = "".join(z2)
                num = int(z1 + "15" + z2 + "7424")
                u1 = num % 111 == 0
                u2 = num % 113 == 0
                u3 = num % 127 == 0
                if u1 == 1 and u2 + u3 == 0:
                    ans.append([num, num // 111])
                if u2 == 1 and u1 + u3 == 0:
                    ans.append([num, num // 113])
                if u3 == 1 and u2 + u1 == 0:
                    ans.append([num, num // 127])
ans = sorted(ans)
for i in ans:
    print(*i)
