from re import *

with open("24_21908.txt") as file:
    data = file.readline()

ans = 0
pattern = r"[1-9A-D][0-9A-D]*[2468BD]"
match = finditer(pattern, data)
match = [i.group() for i in match]
for i in match:
    if int(i, 14) % 2 == 0:
        ans = max(ans, len(i))

print(ans)