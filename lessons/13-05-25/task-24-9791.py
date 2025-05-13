with open("24_9791.txt") as file:
    data = file.readline()

alf = "123456789ABCDEF"
for i in alf:
    data = data.replace(i, "*")
ans = []
cnt = 0
for i in data:
    if i == "*":
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0

print(max(ans))