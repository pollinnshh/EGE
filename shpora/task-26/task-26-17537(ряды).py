with open("26_17537.txt") as file:
    n, m, k = map(int, file.readline().split())
    suitable = [m] * (k + 1)
    for i in file:
        row, col = map(int, i.split())
        suitable[col] = min(suitable[col], row - 1)  # сохраняем место на которое можем сесть

ans = []
for i in range(2, k + 1):
    place1, place2 = suitable[i - 1], suitable[i]  # аппендим подходящий ряд и макс. место из пары
    ans.append([min(place1, place2), i])

print(max(ans))
