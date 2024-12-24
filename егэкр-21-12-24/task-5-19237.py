def conv(num,sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1,10000):
    n1 = conv(n,3)
    if n % 3 == 0:
        n1 = n1 + n1[-2:]
    else:
        summ = sum(map(int,n1))
        n1 = n1 + conv(summ,3)
    r = int(n1,3)
    if r > 220 and r % 2 == 0:
        ans.append(r)
print(min(ans))