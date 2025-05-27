with open("26_4629.txt") as file:
    n = file.readline()
    costs = [int(i) for i in file]

costs = sorted(costs)
mag = sum(costs[int(n) // 4:]) + sum(costs[:int(n) // 4]) // 2
pok = sum(costs[:-int(n) // 4]) + sum(costs[-int(n) // 4:]) // 2

print(pok, mag)


