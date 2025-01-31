def f(a):
    for x in range(1,1000):
        for y in range(1,100):
            f = ((x - y) >= 39) or (y <= x) or (y >= (a - 20))
            if not f:
                return False
    return True
ans = []
for a in range(1,10000):
    if f(a):
        ans.append(a)
print(max(ans))