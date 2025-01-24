def f(a):
    for x in range(1,1000):
        u1 = (a + 7 > x) and (a + x > 7) and (7 + x > a)
        u2 = (36 + 21 > x) and (21 + x > 36) and (36 + x > 21)
        f = u1 <= ((max(x + 5, 14) <= 27) == (not u2))
        if not f:
            return False
    return True
for a in range(1000,1,-1):
    if f(a):
        print(a)
        break