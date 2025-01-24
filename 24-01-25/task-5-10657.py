def conv(num,sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1,10000):
    n1 = conv(n,3)
    if (n1.count("1") + n1.count("2") * 2) % 3 == 0:
        n1 = "20" + n1
    else:
        n1 = "10" + n1
    r = int(n1,3)
    if r < 100:
        ans.append(n)
print(max(ans))
