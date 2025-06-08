with open("26_20815.txt") as file:
    n, s = map(int, file.readline().split())
    astronauts = []
    for i in file:
        ID, b1, b2, b3, b = map(int, i.split())
        astronauts.append([ID, (b1 + b2 + b3 + b), b])

astronauts = sorted(astronauts, key=lambda x: (-x[1], -x[2], x[0]))
print(astronauts[:s])
print(len([i for i in astronauts if i[1] == 279]))


