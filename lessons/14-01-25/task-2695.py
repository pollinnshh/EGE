from itertools import permutations, product


def f(x, y, z, w):
    return (w or y) and (x <= (not z)) and (not w)


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(a1, 0, a2, 0), (1, a3, a4, a5), (1, 1, 0, 0)]
    if len(set(table)) == len(table):
        for p in permutations("xyzw"):
            u = [f(**dict(zip(p, t))) for t in table] == ([1, 1, 1])
            if u:
                print(*p)
