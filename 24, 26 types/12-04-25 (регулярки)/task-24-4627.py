from re import finditer

with open("24_4627.txt") as file:
    data = file.readline()

pattern = r"(NPO|PNO)+"
match = finditer(pattern, data)
match = [i.group() for i in match]
print(len(max(match, key=len)) // 3)
