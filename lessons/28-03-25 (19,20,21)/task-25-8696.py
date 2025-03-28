def prost(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def f(num):
    res = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)
    res = sorted(set(res))

    m = sum(res)
    if len(res) == 0:
        return 0
    if prost(m % 100000):
        return m


count = 0
for i in range(1_273_548, 10 ** 50):
    if f(i):
        print(i, f(i))
        count += 1
        if count == 5:
            break
