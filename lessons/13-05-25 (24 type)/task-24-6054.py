with open("24_6054.txt") as file:
    data = file.readline()

data = data.replace("B", "C")
data = data.replace("CCA", "*")

cnt = 0
ans = []
for i in data:
    if i == "*":
        cnt += 3
    else:
        ans.append(cnt)
        cnt = 0

print(max(ans))