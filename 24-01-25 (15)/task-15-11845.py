def f(a):
    for x in range(1,1000):
        f = (a % x == 0) <= ((x == a) or (x == 1))
        if not f:
            return False
    return True
ans = []
for a in range(1,11_112):
    if f(a):
        ans.append(a)
print(len(ans))