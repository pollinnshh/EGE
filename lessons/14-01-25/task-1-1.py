print("x y z w f")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x <= y) and (z == (w <= x)) and (not w)
                if f:
                    print(x, y, z, w, f)

# def f(x, y, z):
#   print(x, y, z)
#   d = {"x":1,"y":2, "z":3}
#        print(**d)

from itertools import permutations, product


def f(a, b, c, d):
    return (not a) and (not b) or (b == c) or d


for a1, a2, a3, a4 in product([1, 0], repeat=4):
    table = [(a1, a2, 1, a3), (1, 0, a4, 1), (0, 0, 1, 1)]
    if len(set(table)) == len(table):
        for p in permutations("abcd"):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)
