from itertools import *

cnt = 0
for num in product("0123456", repeat=5):
    num = "".join(num)
    chet = sum(int(i) for i in num if int(i) % 2 == 0)
    nechet = sum(int(i) for i in num if int(i) % 2)
    if num[0] != "0":
        if num.count("6") == 1 and chet < nechet:
            cnt += 1
print(cnt)
