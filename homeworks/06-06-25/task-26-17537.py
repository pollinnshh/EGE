with open("26_17537.txt") as file:
    n, m, k = map(int, file.readline().split())
    suitable = [m] * (k + 1)
    for i in file:
        row, place = map(int, i.split())
        suitable[place] = min(suitable[place], row - 1)

ans = []
for i in range(2, k + 1):
    place1, place2 = suitable[i - 1], suitable[i]
    ans.append([min(place1, place2), i])  # аппендим подходящий ряд и макс. место из пары получается

print(max(ans))
