ans = []
for n in range(1,1000):
    n1 = bin(n)[2:]
    if n % 2 == 0:
        n1 = n1 + "01"
    else:
        n1 = "1" + n1 + "1"
    r = int(n1, 2)
    if r > 156:
        ans.append(n)
print(min(ans))