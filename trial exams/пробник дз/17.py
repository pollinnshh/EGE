with open("17_8562.txt") as file:
    num = [int(i) for i in file]
num1 = [k for k in num if len(str(abs(k))) == 2 and str(k)[-1] == "1"]
ans = []
for i in range(len(num) - 1):
    n1, n2 = num[i], num[i + 1]
    u1 = n1 ** 2 < min(num1) ** 2
    u2 = n2 ** 2 < min(num1) ** 2
    u3 = (n1 + n2) >= 0
    if u1 + u2 == 1 and u3:
        ans.append(n1 + n2)
print(len(ans), min(ans))