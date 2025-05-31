with open("26_7602.txt") as file:
    k = int(file.readline())
    n = int(file.readline())
    clients = [list(map(int, i.split())) for i in file]

clients = sorted(clients)
last = 0
cnt = 0
rooms = [0] * (k + 1)
for c in clients:
    for i in range(1, len(rooms)):
        if c[0] >= rooms[i]:
            rooms[i] = c[1] + 1
            cnt += 1
            last = i
            break

print(cnt, last)