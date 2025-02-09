def f(a):
    for x in range(1, 1000):
        b = 80 <= x <= 100
        f = ((x % 17) == 0) <= ((not b) or (a < (x + 30)))
        if not f:
            return False
    return True


ans = []
for a in range(1, 10000):
    if f(a):
        ans.append(a)
print(max(ans))
