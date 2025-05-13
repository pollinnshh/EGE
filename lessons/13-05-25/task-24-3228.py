with open("24_3228.txt") as file:
    data = file.readline()

data = data.replace("AB", "*").replace("AC", "*")
cnt = 0
ans = []
for i in data:
    if i == "*":
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0

print(max(ans))
