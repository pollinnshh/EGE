def f(a):
    for x in range(1,10000):
        f = ((not(x % 7 == 0)) and (x % 13 == 0)) <= (x > a - 40)
        if not f:
            return False
    return True
for a in range(10000,1,-1):
    if f(a):
        print(a)
        break