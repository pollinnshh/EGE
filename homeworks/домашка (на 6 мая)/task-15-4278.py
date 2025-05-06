def f(a):
    for x in range(1, 1000):
        f = (a % 12 == 0) and ((530 % x == 0) <= ((a % x != 0) <= (170 % x != 0)))
        if not f:
            return False
    return True


cnt = 0
for a in range(1, 1001):
    if f(a):
        cnt += 1
print(cnt)
