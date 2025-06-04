def f(a):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = ((x + 2 * y) > a) or (y < x) or (x < 30)
            if not f:
                return False
    return True


for a in range(1000, -1, -1):
    if f(a):
        print(a)
        break
