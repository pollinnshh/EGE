from itertools import *


def f(x, y, z, w):
    return not (x <= z) or (y == w) or y


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(1, 0, a1, a2), (a3, 1, 0, a4), (0, a5, a6, a7)]
    if len(table) == len(set(table)):
        for p in permutations("xzyw"):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)
