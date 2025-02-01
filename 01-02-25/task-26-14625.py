with open("26_14625.txt") as file:
    n = int(file.readline())
    k, r, m = map(int, file.readline().split())
    m *= 2 ** 20
    files = []
    for i in file:
        t, s, e = i.split()
        p = 1
        if e == "mb":
            p = 2 ** 20
        elif e == "kb":
            p = 2 ** 10
        s = int(s) * p
        files.append([int(t), s])

files = sorted(files, key=lambda x: -x[1])
deleted = [0] * (k + 1)
last_file = 0
volume = 0

for file in files:
    if deleted[file[0]] < r:
        deleted[file[0]] += 1
        volume += file[1]
        last_file = file
        if volume >= m:
            break
deleted[last_file[0]] -= 1
volume -= last_file[1]
for file in files[::-1]:
    if deleted[file[0]] < r and volume + file[1] >= m:
        print(sum(deleted) + 1, file)
        break

print(sum(deleted) + 1,file)