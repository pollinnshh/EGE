from itertools import permutations
graf = "BH HF FD DC CE EA AB AH EG GF GC".split()
matrix = "247 148 578 126 38 47 136 235".split()
print(*range(1,9))
for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graf):
        print(*i)