with open("26_19256.txt") as file:
    n = int(file.readline())
    students = [list(map(int, i.split())) for i in file]

students = sorted(students)
ans = []
cnt = 1
for i in range(len(students) - 1):
    st1, st2 = students[i], students[i + 1]
    if st1[1] == st2[1]:
        continue
    if st1[0] == st2[0]:
        if st2[1] - st1[1] == 1:
            cnt += 1
        else:
            cnt = 1
    else:
        cnt = 1
    ans.append([st1[0], cnt])

print(sorted(ans, key=lambda x: (-x[1], x[0]))[0])