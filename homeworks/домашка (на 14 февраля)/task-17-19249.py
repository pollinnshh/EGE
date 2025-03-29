with open("17_19249.txt") as file:
    num = [int(i) for i in file]

ans = []
list = [i for i in num if len(str(abs(i))) == 5 and str(i)[-2:] == "43"]
for i in range(len(num) - 2):
    n1, n2, n3 = num[i:i + 3]
    u1 = n1 in list
    u2 = n2 in list
    u3 = n3 in list
    u4 = n1 ** 2 + n2 ** 2 + n3 ** 2 <= max(list) ** 2
    if u1 + u2 + u3 >= 1 and u4:
        ans.append(n1 ** 2 + n2 ** 2 + n3 ** 2)
print(len(ans), min(ans))
