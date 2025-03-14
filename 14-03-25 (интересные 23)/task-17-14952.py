with open("17_14952.txt") as file:
    num = [int(i) for i in file]

ans = []
max_el = max(i for i in num if str(i)[-3:] == "121")
for i in range(len(num) - 2):
    n1, n2, n3 = num[i], num[i + 1], num[i + 2]
    u1 = len(str(abs(n1))) == 4 and n1 % 2 == 0
    u2 = len(str(abs(n2))) == 4 and n2 % 2 == 0
    u3 = len(str(abs(n3))) == 4 and n3 % 2 == 0
    summ = n1 + n2 + n3
    if u1 + u2 + u3 <= 1 and summ <= max_el:
        ans.append(summ)

print(len(ans), max(ans))