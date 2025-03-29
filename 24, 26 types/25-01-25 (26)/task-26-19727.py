with open("26.2_19727.txt") as file:
    max_massa, n = map(int, file.readline().split())
    num = [int(i) for i in file]
num = sorted(num)
ans_1 = 0
massa = 0
for i in num:
    if massa + i <= max_massa:
        massa += i
        ans_1 += 1
ans_2 = 0
for i in num[::-1]:
    if sum(num[:ans_1 - 1]) + i > max_massa:
        ans_2 += 1
print(ans_1, ans_2)