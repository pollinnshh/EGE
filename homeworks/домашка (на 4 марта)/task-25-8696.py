def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def f(num):
    res = list()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)

    res = sorted(set(res))
    if len(res) <= 1:
        return 0

    m = sum(res)
    if is_prime(m % 100_000):
        return m


count = 0
for i in range(1273548, 10 ** 20):
    if f(i):
        print(i, f(i))
        count += 1
        if count == 5:
            break
