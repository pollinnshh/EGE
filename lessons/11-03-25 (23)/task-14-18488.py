for x in range(1,1000):
    num = 7 ** 666 + 7 ** 333 + 49 ** x - 343
    count = 0
    while num:
        if num % 7 == 6:
            count += 1
        num //= 7
    if count == 49:
        print(x)