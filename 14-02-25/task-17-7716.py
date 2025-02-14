with open("17_7716.txt") as file:
    num = [int(i) for i in file]
nechet = [i for i in num if str(i).count("0") == 0 \
          and str(i).count("2") == 0 and str(i).count("4") == 0 \
          and str(i).count("6") == 0 and str(i).count("8") == 0]
ans = []
for i in range(len(num) - 1):
    n1, n2 = num[i], num[i + 1]
    u1 = n1 not in nechet
    u2 = n2 not in nechet
    u3 = (n1 + n2) > max(nechet)
    if u1 + u2 >= 1 and u3:
        ans.append(n1 + n2)
print(len(ans), max(ans))
