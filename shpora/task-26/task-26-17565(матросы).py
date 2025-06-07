with open("26_17565.txt") as file:
    n, s = map(int, file.readline().split())
    sailors = []
    for i in file:
        ID, b1, b2, b3, b4 = map(int, i.split())
        sailors.append([ID, (b1 + b2 + b3), b4])

sailors = sorted(sailors, key=lambda x: (-x[1], -x[2]))

# 1
print(sailors[:s])
print(sailors[s:s + 2])      # смотрим полупроходной
print(len([i for i in sailors if i[1] == 154]))     # можно посмотреть глазами

# 2
if sailors[s - 1][1] == sailors[s][1]:
    id_last = [sailor[0] for sailor in sailors if sailor[1] > sailors[s - 1][1]][-1]
    cnt = len([1 for sailor in sailors if sailor[1] == sailors[s - 1][1]])
else:
    id_last = sailors[s - 1][0]
    cnt = 0

print(id_last, cnt)
