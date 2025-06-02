with open("26_1207.txt") as file:
    s, n = map(int, file.readline().split())
    files = [int(i) for i in file]

files = sorted(files)
users = []
for file in files:
    if file <= s:
        s -= file
        users.append(file)
    else:
        break

s += users.pop()
files = sorted(files)[::-1]
for file in files:
    if file <= s:
        users.append(file)
        break

print(len(users), users[-1])
