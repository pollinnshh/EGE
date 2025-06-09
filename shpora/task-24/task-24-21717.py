with open("24_21717.txt") as file:
    data = file.readline()

data = data.split("RSQ")
ans = 1000000000
for i in range(len(data) - 129):
    s = "RSQ" + "RSQ".join(data[i:i + 129]) + "RSQ"
    k = data[i + 129]
    cnt = 0
    for j in k:
        cnt += 1
        if j != "Q":
            break
    if not k:
        cnt += 1
    ans = min(ans, len(s) + cnt)

print(ans)
