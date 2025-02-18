with open("17_19486.txt") as file:
    num = [int(i) for i in file]
chis_7 = [i for i in num if str(i)[-1] == "7"]
ans = []
for a in range(len(num) - 1):
    n1, n2 = num[a], num[a + 1]
    u1 = (n1 < 0) and (n2 > 0)
    u2 = (n2 < 0) and (n1 > 0)
    if (u1 or u2) and n1 + n2 < len(chis_7):
        ans.append(n1 + n2)
print(len(ans), max(ans))
