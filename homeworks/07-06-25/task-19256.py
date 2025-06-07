with open("26_19256.txt") as file:
    n = int(file.readline())
    students = [list(map(int, i.split())) for i in file]

students = sorted(students)
ans = []
cnt = 0
for i in range(len(students) - 1):
    st1, st2 = students[i], students[i + 1]
    if st1[0] == st2[0]:
        if st2[1] - st1[1] == 1:
            cnt += 1
        else:
            ans.append([st1[0], cnt])
            cnt = 1
print(sorted(ans, key=lambda x: (-x[1], x[0])))