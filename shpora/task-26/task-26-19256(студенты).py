with open("26_19256.txt") as file:
    n = int(file.readline())
    students = [list(map(int, i.split())) for i in file]

students = sorted(students)
ans = []
cnt = 1
for i in range(n - 1):
    st1, st2 = students[i], students[i + 1]
    if st1[0] == st2[0]:
        if st2[1] - st1[1] == 0:
            continue
        if st2[1] - st1[1] == 1:
            cnt += 1
        else:
            cnt = 1
    else:
        cnt = 1
    ans.append([st1[0], cnt])

ans = sorted(ans, key=lambda x: (-x[1], x[0]))
print(ans[0])


#########################################
# students = {}
# for i in file:
#     ID, num = map(int, i.split())
#     if ID not in students:
#         students[ID] = set()
#     students[ID] |= {num}
#
# for ID in students:
#     students = sorted(students[ID])
#########################################