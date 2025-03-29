def conv(num,sys):
    alf = "0123456789AB"
    res = ""
    while num:
        res += alf[num % sys]
        num //= sys
    return res[::-1]
ans = []
for n in range(1,10000):
    n1 = conv(n,12)
    if n % 3 == 0:
        n1 = "1" + n1 + "B"
    else:
        n1 = "2" + n1 + "0"
    r = int(n1,12)
    if r < 1996:
        ans.append(r)
print(max(ans))
