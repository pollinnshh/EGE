with open("26_6759.txt") as file:
    n = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices)[::-1]
poc = sum(prices) - sum(prices[:n // 3])
shop = sum(prices) - sum(prices[2::3])

print(poc, shop)
