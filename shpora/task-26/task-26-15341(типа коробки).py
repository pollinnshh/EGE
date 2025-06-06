with open("26_15341.txt") as file:
    n = int(file.readline())
    cakes = [int(i) for i in file]

cakes = sorted(cakes)[::-1]
last = cakes[0]
cnt = 1
for cake in cakes:
    if last - cake >= 8:
        last = cake
        cnt += 1
print(cnt, last)
