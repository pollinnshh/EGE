def f(a):
    for x in range(1, 1000):
        f = (x % a == 0) or ((70 <= x <= 90) <= (x % 22 != 0))
        if not f:
            return False
    return True


for a in range(1000, 0, -1):
    if f(a):
        print(a)
        break
