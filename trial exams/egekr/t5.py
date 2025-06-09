def f(n):
    res = ""
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]


for n in range(3, 10000):
    n1 = f(n)
    if n % 3 == 0:
        n1 = n1 + n1[-2:]
    else:
        n1 = n1 + f(n % 3 * 3)
    r = int(n1, 3)
    if r <= 150:
        print(n)
