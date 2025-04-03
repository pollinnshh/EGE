from itertools import *

for p in range(6):
    for z in product("0123456789", repeat=p):
        z = "".join(z)
        st = "20" + z + "23"
        summ = sum(map(int, st))
        if int(st) % 2023 == 0 and summ < 20 and summ % 7 == 0:
            print(st)
