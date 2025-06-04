def f(a):
    for x in range(1, 1000):
        f = (x % a == 0) or ((60 <= x <= 80) <= (x % 22))
        if not f:
            return False
    return True

for a in range(1000, 0, -1):
    if f(a):
        print(a)
        break