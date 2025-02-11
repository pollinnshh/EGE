with open("17_4622.txt") as file:
    num = [int(i) for i in file]

ans = []
min_19 = min(i for i in num if i > 0 and i % 19 == 0)  # то же самое, что и с []
for i in range(len(num) - 1):
    n1, n2 = num[i], num[i + 1]
    u = (n1 + n2) < min_19
    if u:
        ans.append(n1 + n2)
print(len(ans), max(ans))
