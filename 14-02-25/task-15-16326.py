def f(a):
    for x in range(1,1000):
        f = (x % a != 0) <= ((x % 14 ==0) <= (x % 4 != 0))
        if not f:
            return False
    return True
for a in range(1000,1,-1):
    if f(a):
        print(a)
        break