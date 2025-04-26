from re import finditer

with open("24-337.txt") as file:
    data = file.readline()

pattern = r"1[0-9A-D]+"

matches = finditer(pattern, data)
ans = []
for i in matches:
    num = i.group()
    for j in range(len(num) - 1):
        if num[j] != "1":
            continue
        for k in range(j + 1, len(num)):
            if int(num[j:k + 1], 14) % 7 == 0:
                ans.append(len(num[j:k + 1]))

print(max(ans))
