with open("17.txt") as file:
    num = [int(i) for i in file]

ans = []
maxx = max(i for i in num if str(i)[-2:] == "50")
for i in range(len(num) - 2):
    n1, n2, n3 = num[i:i + 3]
    u1 = len(str(abs(n1))) == 5
    u2 = len(str(abs(n2))) == 5
    u3 = len(str(abs(n3))) == 5
    u4 = n1 != n2 and n2 != n3
    u5 = n1 + n2 + n3 <= maxx
    if u1 + u2 + u3 + u4 + u5 == 5:
        ans.append(n1 + n2 + n3)
print(len(ans), max(ans))
