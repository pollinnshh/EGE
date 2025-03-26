def conv(num, sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []
for n in range(1, 10000):
    n1 = conv(n, 4)
    summ = sum(map(int, n1))
    if summ % 2 == 0:
        n1 = n1 + n1[-2:]
    else:
        n1 = "2" + n1 + "0"
    r = int(n1, 4)
    if r % 2 == 0 and r > 120:
        ans.append(r)
print(min(ans))
