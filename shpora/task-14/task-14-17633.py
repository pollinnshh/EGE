for x in range(1, 2030):
    n = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    cnt = 0
    while n:
        if n % 6 == 0:
            cnt += 1
        n //= 6
    if cnt == 202:
        print(x)
