with open("26_17881.txt") as file:
    n = int(file.readline())
    students = []
    for i in file:
        ID, b1, b2, b3, b4 = map(int, i.split())
        students.append([ID, (b1 + b2 + b3 + b4)])


