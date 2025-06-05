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
    ans = []
    for i in res:
        if prost(i):
            ans.append(i)

    s = sum(ans)
    if s != 0 and s % 145 == 0:
        return s


cnt = 0
for i in range(32500_001, 10 ** 10):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 7:
            break
