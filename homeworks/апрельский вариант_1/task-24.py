with open("24_19149.txt") as file:
    data = file.readline()

res = []
data = data.replace("(", " (").replace(")", ") ")
data = data.split()
for i in data:
    u1 = i[0] == "(" and i[-1] == ")"
    u2 = "(+" not in i and "+)" not in i and "++" not in i
    u3 = len(i) > 2
    if u1 and u2 and u3:
        res.append(i)

cnt = 0
for i in res:
    n = i.strip("(").strip(")")
    n1 = n.split("+")
    if sum(map(int, n1)) % 2 == 0:
        cnt = max(len(i), cnt)

print(cnt)
