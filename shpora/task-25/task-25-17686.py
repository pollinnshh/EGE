def f(num):
    res = []
    for i in range(2, int(num * 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)
    res = sorted(set(res))
    for i in res:
        if str(i)[-1] == "7" and i != 7:
            return i


cnt = 0
for i in range(700_000, 10 ** 40):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break
