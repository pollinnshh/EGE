with open("24_4643.txt") as file:
    data = file.readline()

data = data.replace("B", "A").replace("1", "2")
data = data.replace("22A", "*")
cnt = 0
ans = []
for i in data:
    if i == "*":
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0
print(max(ans))