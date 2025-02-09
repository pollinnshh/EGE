def f(a):
    for x in range(1, 10000):
        f = ((a + x) > (700 - a)) and (((a % 100) + (100 % x)) > 50)
        if not f:
            return False
    return True


for a in range(1, 10000):
    if f(a):
        print(a)
        break
