with open("26_7626.txt") as file:
    k = int(file.readline())
    n = int(file.readline())
    bags = [list(map(int, i.split())) for i in file]

bags = sorted(bags)
cnt = 0
last = 0
rooms = [0] * (k + 1)

for b in bags:
    for i in range(1, len(rooms)):
        if b[0] >= rooms[i]:
            cnt += 1
            last = i
            rooms[i] = b[1] + 1
            break
print(cnt, last)