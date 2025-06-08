with open("26_21719.txt") as file:
    n = int(file.readline())
    students = [list(map(int, i.split())) for i in file]

students = sorted(students)
cnt = 1
ans = []
for i in range(n - 1):
    st1, st2 = students[i], students[i + 1]
    if st1[0] == st2[0]:
        if st2[1] == st1[1]:
            continue
        if st2[1] - st1[1] == 2:
            cnt += 1
        else:
            cnt = 1
    else:
        cnt = 1
    ans.append([st1[0], cnt])

print(sorted(ans, key=lambda x: (-x[1], x[0]))[0])
