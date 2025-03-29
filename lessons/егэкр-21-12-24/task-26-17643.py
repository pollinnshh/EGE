with open("input.txt") as file:
    N = int(file.readline())
    product = {}
    for i in file:
        article, price, status = map(int,i.split())
        if article not in product:
            product[article] = [price, 1, status]
        else:
            product[article][1] += 1
            product[article][2] += status

summ = 0
for i in product.values():
    summ += i[0]

sred = summ / len(product)

ans = []
for i in product.values():
    if i[0] > sred:
        ans.append(i)