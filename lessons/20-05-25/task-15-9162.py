def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (not ((x * y) > (a + 13))) <= ((28 * y) > 520) or ((x * 25) > 800)
            if not f:
                return False
    return True

for a in range(-100, 1000):
    if f(a):
        print(a)