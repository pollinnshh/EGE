def f(a):
    for x in range(0,1000):
        for y in range(0,1000):
            f = ((x**2 + y**2) > 1024 - x) or (y < -2 * x + a)
            if not f:
                return False
    return True
for a in range(1,1000):
    if f(a):
        print(a)
        break