def f(a):
    for x in range(1,1000):
        u1 = x % 10 == 5
        u2 = x % 10 == 4
        f = ((not u1) and u2) <= (x > a - 11)
        if not f:
            return False
    return True
for a in range(1000,1,-1):
    if f(a):
        print(a)
        break