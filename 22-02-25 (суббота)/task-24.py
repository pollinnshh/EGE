with open("24-1.txt") as file:
    data = file.readline()

data = data.replace("++", " ").replace("**", " ")
data = data.replace("+*", " ").replace("*+", " ")

for i in "0123456789":                                        ## проверка на незначащие нули
    data = data.replace(f"+0{i}", f"+0{i}")
    data = data.replace(f"*0{i}", f"*0{i}")
    while f"0{i}" in data:
        data = data.replace(f"0{i}", f"{i}")

data = data.split()
ans = 0
for i in data:
    st = i.strip("+").strip("*")
    if eval(st) == 0:
        ans = max(ans, len(st))
print(ans)

### 17:
# for n1, n2, n3 in zip(data, data[1:], data[2:])