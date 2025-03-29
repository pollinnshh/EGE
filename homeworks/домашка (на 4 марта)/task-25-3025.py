def f(num):
    res = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)
    res = sorted(set(res))[::-1]

    d = [i for i in res if i % 2 != 0]
    if len(d) < 6:
        return 0
    return d[5]


cnt = 0
for i in range(200_000_001, 10 ** 20):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break
