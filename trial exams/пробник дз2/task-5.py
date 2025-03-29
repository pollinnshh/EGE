def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for n in range(1,1000):
    n1 = conv(n, 4)
    if (n1.count("1") + n1.count("2") + n1.count("3")) % 2 == 0:
        n1 = n1[:len(n1) // 2] + "0" + n1[len(n1) // 2:]
    r = int(n1)
    if r <= 180:
        print(n)

