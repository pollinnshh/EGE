def f(a):
    for x in range(1, 5000):
        for y in range(1, 5000):
            f = ((x + 2) <= 50) or (y < (x + 10)) or (x >= a)
            if not f:
                return False
    return True


for a in range(1000, 1, -1):
    if f(a):
        print(a)
        break
