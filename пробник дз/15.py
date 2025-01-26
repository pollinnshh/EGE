def f(a):
    for x in range(1,10000):
        for y in range(1,10000):
            u1 = x * y > (a + 13)
            u2 = 28 * y > 520
            u3 = x * 25 > 800
            f = (not u1) <= (u2 or u3)
            if not f:
                return False
    return True
for a in range(1000000,1,-1):
    if f(a):
        print(a)
        break