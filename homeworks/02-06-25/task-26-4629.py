with open("26_4629.txt") as file:
    n = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices)[::-1]
pr_1 = sum(prices) - sum(prices[:n // 4]) // 2

prices = sorted(prices)
pr_2 = sum(prices) - sum(prices[:n // 4]) // 2

print(pr_1, pr_2)
