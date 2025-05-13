with open("24_9845.txt") as file:
    data = file.readline()

data = data.replace("8", "9")
for i in "AB":
    data = data.replace(i, "C")

while "99" in data or "CC" in data:
    data = data.replace("99", "9 9").replace("CC", "C C")

data = data.split()
print(len(max(data, key=len)))
