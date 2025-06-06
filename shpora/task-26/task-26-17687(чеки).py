with open("26_17687.txt") as file:
    n = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices)[::-1]
ans_1 = sum(prices) - sum(prices[:n // 9])
ans_2 = sum(prices) - sum(prices[8::9])

print(ans_1, ans_2)