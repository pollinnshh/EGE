with open("24_4627.txt") as file:
    data = file.readline()

data = data.replace("NPO", "*").replace("PNO", "*")
cnt = 0
ans = []
for i in data:
    if i == "*":
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0

print(max(ans))