with open("26_17643.txt") as file:
    n = int(file.readline())
    products = {}
    average = []
    for i in file:
        art, price, stat = map(int, i.split())
        average.append(price)
        if art not in products:
            products[art] = [0, price, 0]
        if stat == 0:
            products[art][0] += 1
        if stat:
            products[art][2] += 1

average = sum(average) / n
expensive = [i for i in products.values() if i[1] > average]
leader = sorted(expensive, key=lambda x: (-x[0], -x[1], x[2]))[0]
print(leader[0] * leader[1], leader[2])
