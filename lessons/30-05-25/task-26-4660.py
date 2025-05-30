with open("26_4660 (1).txt") as file:
    n = int(file.readline())
    costs = [int(i) for i in file]

costs = sorted(costs)
ch_1 = sum(costs) - sum(costs[:n // 4]) // 2

costs = sorted(costs)[::-1]
ch_2 = sum(costs) - sum(costs[3::4]) // 2
print(ch_2, ch_1)