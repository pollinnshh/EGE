def f(num):
    res = ""
    while num:
        res += str(num % 3)
        num //= 3
    return res[::-1]


ans = []
for n in range(1, 1000):
    n1 = f(n)
    if n % 3 == 0:
        n1 = "1" + n1 + "02"
    else:
        n1 = n1 + f(n % 3 * 4)
    r = int(n1, 3)
    if r < 199:
        ans.append(n)
print(max(ans))
