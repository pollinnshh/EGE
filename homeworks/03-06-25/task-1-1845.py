from itertools import *

matrix = '67 567 456 35 234 123 12'.split()
graph = 'AB BG GE EZ ZD DV VA VB GD'.split()

print(*range(1, 8))
for i in permutations("ABGEZVD"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
