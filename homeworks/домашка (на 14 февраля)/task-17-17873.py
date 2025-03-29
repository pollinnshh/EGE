with open("17_17873.txt") as file:
    num = [int(i) for i in file]

ans = []
for i in range(len(num) - 1):
    n1, n2 = num[i], num[i + 1]
    u1 = n1 % 16 == min(num)
    u2 = n2 % 16 == min(num)
    if u1 + u2 >= 1:
        ans.append(n1 + n2)
print(len(ans), max(ans))