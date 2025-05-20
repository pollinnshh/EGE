from re import *

with open("24_17641.txt") as file:
    data = file.readline()

pattern = r"(([1-9][0-9]*|0)+[+*])+(([1-9][0-9]*|0)+)"
match = finditer(pattern, data)
match = [i.group() for i in match]
res = []
for i in match:
    if eval(i) == 0:
        res.append(len(i))
    else:
        for l in range(len(i)):
            for r in range(len(i), l, -1):
                ps = i[l:r].strip("+*")
                if len(ps) < 2:
                    break
                if ps[0] == "0" and ps[1] in "0123456789":
                    continue
                if eval(ps) == 0:
                    res.append(len(ps))

print(max(res))