from re import *

with open("24_17878.txt") as file:
    data = file.readline()

pattern = r"((([1-9][0-9]*)|0)[*-])*(([1-9][0-9]*)|0)"
match = finditer(pattern, data)
match = [i.group() for i in match]
print(len(max(match, key=len)))
