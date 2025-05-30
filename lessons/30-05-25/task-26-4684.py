with open("26_4684.txt") as file:
    n = int(file.readline())
    costs = [int(i) for i in file]

costs = sorted(costs)[::-1]
pok = sum(costs) - sum(costs[5::6]) // 2

costs = sorted(costs)
sh = sum(costs) - sum(costs[: n // 6]) // 2

print(pok, sh)