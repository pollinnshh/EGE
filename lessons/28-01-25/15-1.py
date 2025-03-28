def f(a):
    for x in range(1,1000):
        f = ((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (a <= x)
        if not f:
            return False
    return True
for a in range(1,10000):
    if f(a):
        print(a)