with open("24_3584.txt") as file:
    data = file.readline()

data = data.replace("BA", "*").replace("DA", "*")
cnt = 0
ans = []
for i in data:
    if i == "*":
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0

print(max(ans))