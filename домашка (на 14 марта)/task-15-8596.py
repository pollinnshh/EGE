def f(a):
    for x in range(1000):
        for y in range(1000):
            f = (x >= 11) or (3 * x < y) or (x * y < a)
            if not f:
                return 0
    return 1

for a in range(1000):
    if f(a):
        print(a)
        break