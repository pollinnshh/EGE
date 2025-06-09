def f(n):
    res = ""
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]


for n in range(1, 10000000):
    s = ""
    n1 = f(n)
    for i in n1:
        if i == "0":
            s += "2"
        elif i == "2":
            s += "0"
        else:
            s += "1"

    while len(s) > 1 and s[0] == "0":
        s = s[1:]

    d = int(s, 3)
    r = abs(n - d)
    if r == 1_864_246:
        print(n)
        break
