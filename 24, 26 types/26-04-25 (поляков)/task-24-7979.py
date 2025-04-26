from re import *

with open("24-314.txt") as file:
    data = file.readline()

pattern = r"(?<=F)[1-7][0-7]*([+|*][1-7][0-7]*)+"
matches = finditer(pattern, data)

ans = [i.group() for i in matches]
max_len = len(max(ans, key=len))
for num in ans:
    if len(num) == max_len:
        res = ""
        numb = ""
        for i in num:
            if i in "01234567":
                numb += i
            else:
                res +=

