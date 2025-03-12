def f(a):
    for x in range(10000):
        f = ((x & 52 != 0) and (x & 36 == 0)) <= (not (x & a == 0))
        if not f:
            return 0
    return 1

for a in range(10000):
    if f(a):
        print(a)
        break