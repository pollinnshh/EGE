with open("17_18582.txt") as file:
    num = [int(i) for i in file]

ans = []
for i in range(len(num) - 2):
    n1, n2, n3 = num[i:i+3]
    u1 = str(n1 + n2 + n3)[-1] == str(min(num))[-1]
    u2 = n1 < 0 and n2 < 0
    u3 = n1 < 0 and n3 < 0
    u4 = n2 < 0 and n3 < 0
    if u1 and (u2 or u3 or u4):
        ans.append(abs(n1 + n2 + n3))
print(len(ans), max(ans))
