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
    for i in res:
        if prost(i) and str(i)[-3:] == "777":
            return i


count = 0
for n in range(55000001, 10 ** 30):
    if f(n):
        count += 1
        print(n, f(n))
        if count == 4:
            break
