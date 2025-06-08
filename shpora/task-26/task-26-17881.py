with open("26_17881.txt") as file:
    n = int(file.readline())
    students = []
    failed = []
    for i in file:
        ID, b1, b2, b3, b4 = map(int, i.split())
        if b1 == 2 or b2 == 2 or b3 == 2 or b4 == 2:
            failed.append([ID, (str(b1) + str(b2) + str(b3) + str(b4)).count("2")])
        else:
            students.append([ID, (b1 + b2 + b3 + b4) / 4])

students = sorted(students, key=lambda x: (-x[1], x[0]))
m = students + failed
print(m[:n // 4][-1][0])
print(sorted([student for student in failed if student[1] > 2])[0][0])
