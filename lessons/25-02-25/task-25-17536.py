def f(num):
    res = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)
    res = sorted(res)

    if len(res) <= 1:
        return 0

    m = min(res) + max(res)
    if str(m)[-1] == "4":
        return m

cnt = 0
for i in range(800_001, 10 ** 20):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break