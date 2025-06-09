from re import *

with open("24_20813.txt") as file:
    data = file.readline()

pattern = r"((([789][0789]*)|0)[-*])+(([789][0789]*)|0)"
match = finditer(pattern, data)
match = [i.group() for i in match]
print(len(max(match, key=len)))
