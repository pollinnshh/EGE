with open("26_17786.txt") as file:
    n, max_massa = map(int, file.readline().split())
    watermelons = [int(i) for i in file if 7000 <= int(i) <= 12000]
watermelons = sorted(watermelons)[::-1]
max_massa = max_massa * 1000
ans_1 = 0
mass = 0
ans_2 = []
for i in watermelons:
    if mass + i < max_massa:
        ans_1 += 1
        mass += i
        ans_2.append(i)
print(ans_1, min(ans_2))