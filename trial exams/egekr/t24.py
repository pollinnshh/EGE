with open("24_21717.txt") as file:
    data = file.readline()

ans = 1000000000
data = data.split("RSQ")
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
    ans = min(len(s) + cnt, ans)

print(ans)
