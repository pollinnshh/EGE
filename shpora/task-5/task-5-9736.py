ans = []
for n in range(1, 1000):
    n1 = bin(n)[2:]
    if n % 3 == 0:
        n1 = n1 + n1[-3:]
    else:
        n1 = n1 + bin(n % 3 * 3)[2:]
    r = int(n1, 2)
    if r <= 170:
        ans.append(r)

print(max(ans))
