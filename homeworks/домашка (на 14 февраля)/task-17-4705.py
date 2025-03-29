with open("17_4705.txt") as file:
    num = [int(i) for i in file]

ans = []
list = [i for i in num if str(i)[-1:] == "3"]
for i in range(len(num) - 1):
    n1, n2 = num[i], num[i + 1]
    u1 = n1 in list
    u2 = n2 in list
    u3 = n1 ** 2 + n2 ** 2 >= max(list) ** 2
    if u1 + u2 == 1 and u3:
        ans.append(n1 ** 2 + n2 ** 2)
print(len(ans), max(ans))