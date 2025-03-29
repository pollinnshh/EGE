from itertools import *

def f(x, y, z, w):
    return ((x <= z) <= w) or (not y)

for a1, a2, a3, a4, a5, a6, a7 in product([0,1], repeat=7):
    table = [(a1, a2, 1, a3), (a4, 0, a5, a6), (a7, 1, 0, 0)]
    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)