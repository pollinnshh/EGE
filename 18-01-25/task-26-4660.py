with open("26_4660.txt") as file:
    n = int(file.readline())
    prices = [int(i) for i in file]
prices = sorted(prices)[::-1]
skidka_mag = sum(prices[:3 * len(prices) // 4]) + sum([b // 2 for b in prices[3 * len(prices) // 4:]])
skidka_pok =  + sum([a // 2 for a in prices[3::4]])
print(skidka_mag)
