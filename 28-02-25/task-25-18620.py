def f(num):
    res = list()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)
    res = sorted(set(res))

    if len(res) < 2:
        return 0

    m = res[-2] + res[-1]
    if str(m)[-4:] == "1214":
        return m

for i in range(112_500_000, 112_550_001):
    if f(i):
        print(i)

# https://kompege.ru/variant?kim=25085301