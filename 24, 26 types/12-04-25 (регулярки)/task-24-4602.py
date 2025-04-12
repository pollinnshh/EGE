from re import finditer

with open("24_4602.txt") as file:
    data = file.readline()

pattern = r"([BCD][AO])+"
match = finditer(pattern, data)
match = [i.group() for i in match]
print(len(max(match, key=len)) // 2)  # кол-во пар надо
