with open("17_12249.txt") as file:
    num = [int(i) for i in file]

ans = []
max_ = max(i for i in num if len(str(abs(i))) == 5 and str(i)[-1] == "3")
for i in range(len(num) - 2):
    n1, n2, n3 = num[i:i + 3]
    u1 = str(n1)[-1] == "3"
    u2 = str(n2)[-1] == "3"
    u3 = str(n3)[-1] == "3"
    u4 = n1 + n2 + n3 <= max_
    if u1 + u2 + u3 >= 1 and u4:
        ans.append(n1 + n2 + n3)

print(len(ans), max(ans))