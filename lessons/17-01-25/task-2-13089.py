from itertools import permutations, product


def f(x, y, z, w, u):
    return ((z <= w) and (y == (not x)) <= (u == (y or z)))


for a1, a2, a3, a4,a5,a6,a7,a8 in product([0, 1], repeat=8):
    table = [(0,a1, 0, 0, 0), (0, a2, a3, 0,0), (a4, 0, 0, 0,a5),(0,0,a6,a7,a8)]
    if len(set(table)) == len(table):
        for p in permutations("xzywu"):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0,0]
            if u:
                print(*p)