with open("26_6641.txt") as file:
    n, m = map(int, file.readline().split())
    products = []
    for i in file:
        num, let = i.split()
        products.append([int(num), let])

products = sorted(products)

prod_S = []
prod_W = []
for p in products.copy():
    if p[0] <= m:
        m -= p[0]
        if p[1] == "S": prod_S.append(p[0])
        if p[1] == "W": prod_W.append(p[0])
        products.remove(p)

for p in products:
    if p[-1] == "S" and m + prod_W[-1] - p[0] >= 0:
        m += prod_W[-1] - p[0]
        prod_S.append(p[0])
        prod_W.pop()

print(len(prod_S), m)
