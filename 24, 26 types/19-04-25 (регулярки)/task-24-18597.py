from re import *

with open("24_18597.txt") as file:
    data = file.readline()

pattern = r"[1-9][0-9]{3}[.][0-9]+[&][1-9][0-9]{3}[.][0-9]+"
matches = finditer(pattern, data)
match = [i.group() for i in matches]
print(len(max(match, key=len)))
