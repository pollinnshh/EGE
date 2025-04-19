from re import *

with open("24_18284.txt") as file:
    data = file.readline()

pattern = r"L[^L]*?O.*?V.*?E"
matches = finditer(pattern, data)
match = [i.group() for i in matches]
print(len(min(match, key=len)))
