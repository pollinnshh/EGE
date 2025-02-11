with open("17_9786.txt") as file:
    num = [int(i) for i in file]

max_25 = max(i for i in num if str(i)[-2:] == "25")
ans = []
for i in range(len(num) - 2):
    n1, n2, n3 = num[i:i + 3]
    u1 = 1000 <= abs(n1) <= 9999
    u2 = 1000 <= abs(n2) <= 9999
    u3 = 1000 <= abs(n3) <= 9999
    u4 = (n1 + n2 + n3) <= max_25
    if u1 + u2 + u3 <= 2 and u4:
        ans.append(n1 + n2 + n3)
print(len(ans), max(ans))

