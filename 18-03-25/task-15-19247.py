from functools import lru_cache

@lru_cache(None)
def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = ((x - 3 * y) < a) or (y > 400) or (x > 56)
            if not f:
                return 0
    return 1

for a in range(1, 10000):
    if f(a):
        print(a)
        break

for i in range(800):
    f(i)
print(f(707) - f(716))