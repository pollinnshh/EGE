with open("26_4684.txt") as file:
    n = file.readline()
    costs = [int(i) for i in file]

costs = sorted(costs)[::-1]
mag = sum(costs) - sum(costs[5::6]) // 2
pok = sum(costs[:-int(n) // 6]) + sum(costs[-int(n) // 6:]) // 2

print(mag, pok)