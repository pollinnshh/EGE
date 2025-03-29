def conv(num,sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(10,1000):
    n1 = conv(n, 3)
    if n % 4 == 0:
        n1 = n1 + n1[-3:]
    else:
        n1 = "1" + n1 + "20"
    r = int(n1, 3)
    if r > 423:
        ans.append(r)
print(min(ans))


