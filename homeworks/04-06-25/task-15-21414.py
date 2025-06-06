def f(a):
    for x in range(0, 10000):
        for y in range(0, 10000):
            f = (5 < y) or (x > 32) or ((x + 2 * y) < a)
            if not f:
                return False
    return True

for a in range(0, 1000):
    if f(a):
        print(a)
        break