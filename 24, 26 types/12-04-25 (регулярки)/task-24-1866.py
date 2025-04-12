from re import findall

with open("24_1866.txt") as file:
    data = file.readline()

pattern = r"(?<=ad|da)\w+?(?=ad|da)"
match = findall(pattern, data)
print(len(max(match, key=len)) + 2)  # т.к a и d теряются
