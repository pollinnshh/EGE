ans = []
for n in range(10000):
    n1 = oct(n)[2:]
    if n % 2 == 0:
        n1 = n1 + "7"
    else:
        n1 = n1 + oct(1 * 2)[2:]
    r = int(n1,8)
    if r <= 313:
        ans.append(n)
print(max(ans))