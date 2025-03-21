def f(num, sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for n in range(1, 1000):
    n1 = f(n, 3)
    summ = sum(map(int, n1))
    if summ % 2 == 0:
        n1 = "12" + n1[2:] + "0"
    else:
        n1 = "10" + n1[2:] + "2"
    r = int(n1, 3)
    if r > 105:
        print(n)
        break