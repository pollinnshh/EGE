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

    if sum(ans) != 0 and sum(ans) % 145 == 0:
        return sum(ans)


count = 0
for i in range(32_500_001, 10 ** 40):
    if f(i):
        print(i, f(i))
        count += 1
        if count == 7:
            break
