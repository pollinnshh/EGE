from itertools import *


def f(z, x, y, w):
    return (y <= (not (x <= z))) or w


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(a1, 0, a2, a3), (0, 1, a4, a5), (1, a6, a7, 0)]
    if len(table) == len(set(table)):
        for p in permutations("xzyw"):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)
