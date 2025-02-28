with open("17_12450.txt") as file:
    num = [int(i) for i in file]

ans = []
osob = min(i for i in num if i % 52 == 0)
for i in range(len(num) - 2):
    n1, n2, n3 = num[i:i+3]
    summ = n1 % 113 + n2 % 113 + n3 % 113
    if summ == osob:
        ans.append(n1 + n2 + n3)
print(len(ans), max(ans))
