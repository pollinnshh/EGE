from itertools import *

matrix = "56 378 26 68 17 134 258 247".split()
graph = "AC CF FD DH HG GA AB BC BE ED".split()

print(*range(1, 9))
for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
