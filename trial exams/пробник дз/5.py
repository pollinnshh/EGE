def conv(num, sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []
for n in range(1, 10000):
    n1 = conv(n, 3)
    if n % 3 == 0:
        n1 = n1 + n1[-2:]
    else:
        n1 = n1 + conv(n % 3 * 5, 3)
    r = int(n1, 3)
    if r > 133:
        ans.append(r)
print(min(ans))
