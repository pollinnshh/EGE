with open("17_4597.txt") as file:
    num = [int(i) for i in file]

ans = []
for i in range(len(num) - 1):
    n1, n2 = num[i], num[i + 1]
    if n1 % 117 == min(num) or n2 % 117 == min(num):
        ans.append(n1 + n2)
print(len(ans), max(ans))
