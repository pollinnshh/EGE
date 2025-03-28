def conv(num, sys):
    res = ""
    while num:
        res += str(num %  sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 1000):
    n1 = conv(n, 3)
    summ = sum(map(int, n1))
    if summ % 2 == 0:
        n1 = "1" + n1 + "2"
    else:
        n1 = "2" + n1 + "0"
    r = int(n1, 3)
    if r > 100:
        ans.append(r)
print(min(ans))