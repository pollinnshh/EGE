with open("26_17537.txt") as file:
    n, m, k = map(int, file.readline().split())
    places = [list(map(int, i.split())) for i in file]

places = sorted(places, key=lambda x: (-x[0], x[1]))

pole = [m + 1] * (k + 1)
for r, m in places:
    pole[m] = r

ans = []
for i in range(1, len(pole) - 1):
    p1, p2 = pole[i], pole[i + 1]
    ans.append([min(p1, p2) - 1, i + 1])

print(max(ans))
