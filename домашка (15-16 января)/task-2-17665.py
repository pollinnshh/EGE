## 1
from itertools import product, permutations


def f(x, y, z, w):
    return (z <= (not (y <= x))) or w


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(a1, 1, a2, a3), (a4, a5, 0, 0), (a6, 0, 1, a7)]
    if len(set(table)) == len(table):
        for p in permutations("xyzw"):
            u = [f(**dict(zip(p, t))) for t in table] == ([0, 0, 0])
            if u:
                print(*p)

## 2
print("x y z w f")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (z <= (not (y <= x))) or w
                if not f:
                    print(x, y, z, w, f)
