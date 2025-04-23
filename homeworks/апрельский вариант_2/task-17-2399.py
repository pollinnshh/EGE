with open("17_2399.txt") as file:
    num = [int(i) for i in file]

ans = []
summm = []
n = [i for i in num if i % 35 == 0]
for i in n:
    s = sum(map(int, str(i)))
    summm.append(s)
for i in range(len(num) - 1):
    n1, n2 = num[i], num[i + 1]
    u1 = n1 > sum(summm)
    u2 = n2 > sum(summm)
    u3 = hex(n1)[-2:] == "ef"
    u4 = hex(n2)[-2:] == "ef"
    if u2 and u3:
        ans.append(n1 + n2)

print(len(ans), min(ans))