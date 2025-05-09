from itertools import *

for p in range(3):
    for z in product("0123456789", repeat=p):
        for v1 in "0123456789":
            for v2 in "0123456789":
                for v3 in "0123456789":
                    z = "".join(z)
                    n = "1" + v1 + "1" + v2 + "1" + v3 + "1" + z + "1"
                    sum_ = sum(map(int, n))
                    n = int(n)
                    if n <= 10 ** 10:
                        if n % 2023 == 0 and sum_ == 22:
                            print(n)
