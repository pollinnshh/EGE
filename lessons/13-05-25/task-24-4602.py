with open("24_4602.txt") as file:
    data = file.readline()

data = data.replace("A", "O")
data = data.replace("B", "D").replace("C", "D")

data = data.replace("DO", "*")
cnt = 0
ans = []
for i in data:
    if i == "*":
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0
print(max(ans))