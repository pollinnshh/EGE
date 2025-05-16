ans = []
for n in range(100, 1001):
    n1 = bin(n)[2:]
    n1 = n1.replace("0", "")
    r = int(n1, 2)
    ans.append(r)

print(len(set(ans)))
