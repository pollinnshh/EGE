from re import *
from string import *

with open("24_17641.txt") as file:
    data = file.readline()

num = r"([1-9][0-9]*|0)"
pattern = rf"{num}([+*]{num})+"

match = finditer(pattern, data)
data = [i.group() for i in match]

ans = 0
for i in data:
    if eval(i) == 0:
        ans = max(ans, len(i))
    elif len(i) > ans:
        for l in range(len(i)):
            for r in range(len(i), l, -1):
                sub_str = i[l:r].strip("+*")
                if len(sub_str) < 2 or sub_str[0] == "0" and sub_str[1] in digits:
                    break
                if eval(sub_str) == 0:
                    ans = max(ans, len(sub_str))
                    break

print(ans)


