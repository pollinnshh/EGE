def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for n in range(1, 1000):
    n1 = conv(n, 5)
    if len(n1) % 2 == 0:
        n1 = n1[len(n1) // 2:] + n1[:len(n1) // 2]
    else:
        n1 = n1 + str(n % 5)
        n1 = n1[len(n1) // 2:] + n1[:len(n1) // 2]
    r = int(n1, 5)
    if r > 50:
        print(n)
        break
