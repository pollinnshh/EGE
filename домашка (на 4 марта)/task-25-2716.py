def f(num):
    res = []
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            res.append(i)

    res = sorted(set(res))
    if len(res) < 3:
        return 0

    s = res[-1] + res[-2] + res[-3]
    if s % 2022 == 0 and s != num:
        return s

cnt = 1
for i in range(1_200_001,1,-1):
    if f(i):
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break