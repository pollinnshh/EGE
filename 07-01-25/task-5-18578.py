def conv(num,sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1000):
    n1 = conv(n,4)
    if n % 4 == 0:
        n1 = "2" + n1 + "03"
    else:
        n1 = n1 + conv(n % 4 * 5,4)
    r = int(n1,4)
    if r <= 567:
        ans.append(n)
print(max(ans))