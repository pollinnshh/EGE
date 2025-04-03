def f(num):
    res = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)

    res = sorted(set(res))[::-1]
    if len(res) < 7:
        return 0

    d = res[6]
    return [d, len(res)]


cnt = 0
for i in range(400_000_001, 10 ** 50):
    if f(i):
        print(*f(i))
        cnt += 1
        if cnt == 5:
            break
