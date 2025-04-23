with open("24.5_19717.txt") as file:
    data = file.readline()

data = data.split("M")
cnt = 0
for i in range(len(data) - 279):
    s = "M".join(data[i:i + 279])
    cnt = max(cnt, len(s))

print(cnt)
