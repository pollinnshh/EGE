def f(a):
    for x in range(1, 500):
        for y in range(1, 500):
            for z in range(1, 500):
                f = (((z % 115) == 0) or ((y % 78) == 0) or ((x % 51) == 0)) <= ((x % a) == 0)
                if not f:
                    return False
    return True


ans = []
for a in range(1, 100):
    if f(a):
        ans.append(a)
print(max(ans))
