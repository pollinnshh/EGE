with open("17_17636.txt") as file:
    num = [int(i) for i in file]

ans = []
max_el = max(i for i in num if str(i)[-1] == "3" and len(str(abs(i))) == 3)
for i in range(len(num) - 2):
    n1, n2, n3 = num[i:i + 3]
    u1 = str(n1)[-1] == "3" and len(str(abs(n1))) == 3
    u2 = str(n2)[-1] == "3" and len(str(abs(n2))) == 3
    u3 = str(n3)[-1] == "3" and len(str(abs(n3))) == 3
    if (u1 + u2 + u3) >= 1 and n1 + n2 + n3 < max_el:
        ans.append(n1 + n2 + n3)

print(len(ans), max(ans))
