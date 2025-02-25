def f(num):
    res = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)
    res = sorted(set(res))

    for i in res:
        if str(i)[-1] == "8" and i != 8:
            return i
    return 0


cnt = 0
for i in range(500_001, 10 ** 20):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break

# res = set()
# for i in range(2, int(num ** 0.5) + 1):
#    if num % i == 0:
#        res |= {i, num // i}
# res = sorted(res)
