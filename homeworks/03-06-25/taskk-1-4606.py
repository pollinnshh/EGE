from itertools import *

matrix = "68 47 45 237 368 15 248 157".split()
graph = "AC CE EG GF FA CD DH HE AB BF".split()

print(*range(1, 9))
for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for y, x in graph):
        print(*i)
