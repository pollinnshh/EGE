with open("26_2651.txt") as file:
    n = file.readline()
    marks = [list(map(int, i.split())) for i in file]

marks = sorted(marks)
s = [[0] * 9 for i in range(1992)]
for mark in marks:
    year = mark[0]
    t = mark[1]
    s[year][t] += 1

cnt = []
for i in range(1961, 1992):
    cnt.append(s[i].count(0) - 1)

print(sum(cnt), cnt)
