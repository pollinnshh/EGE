from re import *

with open("24_17563.txt") as file:
    data = file.readline()

pattern = r"(([789][0789]*)[-*])+([789][0789]*)"
match = finditer(pattern, data)
match = [i.group() for i in match]
print(len(max(match, key=len)))