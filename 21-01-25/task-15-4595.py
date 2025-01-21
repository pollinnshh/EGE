def f(A):
    for x in range(1,1000):
        f1 = (x % 2 == 0) <= (x % 3 != 0) or (x + A >= 80)
        if not f1:
            return False
    return True
for A in range(1,1000):
    if f(A):
        print(A)
        break


























