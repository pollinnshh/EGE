with open("26_17643.txt") as file:
    n = int(file.readline())
    products = {}
    average = []
    for i in file:
        art, price, status = map(int, i.split())
        average.append(price)
        if art not in products:
            products[art] = [0, price, 0]
        if status == 1:
            products[art][2] += 1   # кол-во остатков
        else:
            products[art][0] += 1  # кол-во проданных

average = sum(average) / len(average)  # средняя цена
products = [i for i in products.values() if i[1] > average]  # находим в словаре и сохраняем в список дорогие товары

products = sorted(products, key=lambda x: (-x[0], -x[1], x[2]))
leader = products[0]

print(leader[0] * leader[1], leader[2])