for x in range(2005, 1, -1):
    n = 43 ** 56 + 113 ** 841 - x
    chet = 0
    nechet = 0
    cnt = 0
    while n:
        if n % 4 == 2:
            cnt += 1
        if str(n % 4) in "02468":
            chet += 1
        if str(n % 4) in "13579":
            nechet += 1
        n //= 4
    if cnt <= 712 and chet % 2 == 0 and nechet % 2 == 0:
        print(x)
        break
