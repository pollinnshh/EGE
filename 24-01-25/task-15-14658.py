def f(a):
    for x in range(1,10000):
        f = ((x % 12 == 0) <= (not(x % 42 == 0))) or (x + a >= 4096)
        if not f:
            return False
    return True
for a in range(1,10000):
    if f(a):
        print(a)
        break