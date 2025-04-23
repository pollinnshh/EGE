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
    if len(res) < 1:
        return 0

    if prost(m % 100000):
        return m


cnt = 0
for i in range(1273548, 10 ** 20):
   if f(i):
       print(i, f(i))
       cnt += 1
       if cnt == 5:
           break