ans = []
for n in range(1, 1000):
    n1 = bin(n)[2:]
    summ1 = n1.count("1")
    n1 = n1 + str(summ1 % 2)
    summ2 = n1.count("1")
    n2 = n1 + str(summ2 % 2)
    r = int(n2, 2)
    if r > 75:
        ans.append(r)

print(min(ans))
