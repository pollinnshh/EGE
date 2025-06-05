def f(num):
    res = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)
    res = sorted(set(res))
    if len(res) < 2:
        return 0

    m = max(res) + min(res)
    if str(m)[-1] == "4":
        return m


cnt = 0
for i in range(700_001, 10 ** 30):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break
