with open("17_9748.txt") as file:
    num = [int(i) for i in file]
max_15 = max(i for i in num if str(i)[-2:] == "15")
ans = []
for i in range(len(num) - 2):
    n1, n2, n3 = num[i], num[i + 1], num[i + 2]  # num[i:i + 3]
    u1 = len(str(n1)) == 4
    u2 = len(str(n2)) == 4
    u3 = len(str(n3)) == 4
    u4 = (n1 + n2 + n3) >= max_15
    if u1 + u2 + u3 == 1 and u4:
        ans.append(n1 + n2 + n3)
print(len(ans), max(ans))


