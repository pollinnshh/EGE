for x in range(1, 2006):
    num = 4 ** 163 * 5 + 12 ** 62 - x
    count1 = 0
    count4 = 0
    while num:
        if num % 5 == 4:
            count4 += 1
        if num % 5 == 1:
            count1 += 1
        num //= 5
    if count4 > count1:
        print(x)