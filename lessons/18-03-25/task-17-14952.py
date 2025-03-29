with open("17_14952.txt") as file:
    num = [int(i) for i in file]

ans = []
max_el = max(i for i in num if str(i)[-3:] == "121")
for i in range(len(num) - 2):
    n1, n2, n3 = num[i:i + 3]
    u1 = n1 % 2 == 0 and len(str(abs(n1))) == 4
    u2 = n2 % 2 == 0 and len(str(abs(n2))) == 4
    u3 = n3 % 2 == 0 and len(str(abs(n3))) == 4
    if u1 + u2 + u3 <= 1 and (n1 + n2 + n3) <= max_el:
        ans.append(n1 + n2 + n3)
print(len(ans), max(ans))
