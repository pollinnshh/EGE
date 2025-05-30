with open("26_1868.txt") as file:
    n = int(file.readline())
    seats = [list(map(int, i.split())) for i in file]

seats = sorted(seats, key=lambda x: (-x[0], x[1]))
for s1, s2 in zip(seats, seats[1:]):
    if s1[0] == s2[0]:
        if s2[1] - s1[1] == 3:
            print(s1[0], s1[1] + 1)
            break