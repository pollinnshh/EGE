with open("24_15339.txt") as file:
    data = file.readline()

data = data.replace("A", "C").replace("B", "C")
data = data.replace("6", "9").replace("7", "9").replace("8", "9")
while "CC" in data and "99" in data:
    data = data.replace("99", "9 9").replace("CC", "C C")

s = data.split()
print(len(max(s, key=len)))
