with open("17_6791.txt") as file:
    num = [int(i) for i in file]

ans = []
min_ = min(i for i in num if str(i)[-2:] == "68")
for i in range(len(num) - 1):
    n1, n2 = num[i], num[i + 1]
    u1 = str(n1)[-2:] == "68"
    u2 = str(n2)[-2:] == "68"
    u3 = (n1 ** 2 + n2 ** 2) >= min_ ** 2
    if u1 + u2 == 1 and u3:
        ans.append(n1 ** 2 + n2 ** 2)
print(len(ans), max(ans))
