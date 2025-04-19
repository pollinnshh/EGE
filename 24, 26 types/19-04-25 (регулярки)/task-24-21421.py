from re import *

with open("24_21421.txt") as file:
    data = file.readline()

pattern = r"[1-9AB][0-9AB]*[02468A]"
matches = finditer(pattern, data)
match = [i.group() for i in matches]
print(len(max(match, key=len)))
