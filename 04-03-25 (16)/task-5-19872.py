def conv(num, sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for i in range(1, 1000):
    n = conv(i, 7)
    if i % 2 == 0:
        n = "52" + n + "1"
    else:
        n = n[-1] + n[1:-1] + n[0] + "15"

    while n[0] == "0":
        n = n[1:]
    ## n = n.strip("0")

    if len(n) == 4:
        print(i)
