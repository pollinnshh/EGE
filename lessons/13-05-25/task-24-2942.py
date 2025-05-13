with open("24_2942.txt") as file:
    data = file.readline()

data = data.replace("AC", "*").replace("AB", "*")
cnt = 0
ans = []
for i in data:
    if i == "*":
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0

print(max(ans))