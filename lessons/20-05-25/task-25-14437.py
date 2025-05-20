def f(num):
    res = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)

    res = sorted(set(res))
    if len(res) < 1:
        return False

    m = sum(res) // len(res)
    if str(m)[-3:] == "313":
        return m


cnt = 0
for i in range(700000, 1, -1):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 7:
            break
