def f(num):
    res = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)

    res = sorted(set(res))
    if max(res) % 7 == 0:
        return max(res)


cnt = 0
for i in range(10 ** 9 + 1, 10 ** 30):
    if str(i) == str(i)[::-1] and f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break
