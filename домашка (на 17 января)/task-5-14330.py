for num in range(10000, 100000):
    u2 = 1
    num1 = list(str(num))
    u1 = (int(min(num1)) + int(max(num1))) ** 2
    chet = [int(i) for i in num1 if int(i) % 2 == 0]
    for p in chet:
        u2 *= int(p)
    res = str(u1) + str(u2)
    if res == "12116":
        print(num)
        break
