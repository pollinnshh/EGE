k = [i ** 2 for i in range(1, 10000)]


def f(num):
    res = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)

    res = sorted(set(res))
    if len(res) < 3:
        return False

    s = res[-1] + res[-2] + res[-3]
    if s in k:
        return s


for i in range(10_000_001, 10 ** 50):
    if f(i):
        print(f(i))
