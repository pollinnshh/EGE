from re import *

with open("24-335.txt") as file:
    data = file.readline()

pattern = r"([(][1-9][0-9]*[^5|0][+|-][1-9][0-9]*[5|0][)])+"
matches = finditer(pattern, data)
print(len(max([i.group() for i in matches], key=len)))
