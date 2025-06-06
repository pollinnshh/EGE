def f(num):
    res = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)
    res = sorted(set(res))
    r = sum(res)
    if str(r)[-1] == "9":
        return r


cnt = 0
for i in range(500_001, 10 ** 10):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break
