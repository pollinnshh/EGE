with open("26_16390.txt") as file:
    max_V, n = map(int, file.readline().split())
    packages = [int(i) for i in file]
packages = sorted(packages)
ans_1 = 0
mass = 0
last_box = 0
for i in packages:
    if mass + i <= max_V:
        mass += i
        ans_1 += 1
        last_box = i
mass -= last_box
for i in packages[::-1]:
    if mass + i <= max_V:
        last_box = i
        break
print(ans_1, last_box)
