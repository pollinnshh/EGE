with open("26_4629.txt") as file:
    n = file.readline()
    costs = [int(i) for i in file]

costs = sorted(costs)
sh = sum(costs) - sum(costs[:int(n) // 4]) // 2

costs = sorted(costs)[::-1]
cust = sum(costs) - sum(costs[:int(n) // 4]) // 2

print(cust, sh)
