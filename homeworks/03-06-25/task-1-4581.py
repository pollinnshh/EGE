from itertools import *

matrix = "37 367 125 56 34 247 126".split()
graph = "AD DE EG GC CF FA AB BE FB".split()

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
