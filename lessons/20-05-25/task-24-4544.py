with open("24_4544.txt") as file:
    data = file.readline()

data = data.split("XIX")
print(len(max(data, key=len)) + 4)