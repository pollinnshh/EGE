def f(b):
    for x in range(1,1000):
        f = ((x & 500 != 0) and (x & 200 == 0)) <= (not (x & b == 0))
        if not f:
            return False
    return True
for b in range(1,10000):
    if f(b):
        print(b)