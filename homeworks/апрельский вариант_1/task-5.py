def conv(num, sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for n in range(1, 100000):
    n1 = conv(n, 3)
    if n % 5 == 0:
        n1 = n1 + n1[-3:]
    else:
        n1 = n1 + conv(n % 5 * 5, 3)
    r = int(n1, 3)

    if r < 5496:
        print(n)
