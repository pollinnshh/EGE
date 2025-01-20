from itertools import permutations

grapf = "BE BD BC ED EH DG GA GF AF FH HC".split()
matrix = "234 157 147 138 268 58 23 456".split()
print(*range(1, 9))
for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in grapf):
        print(*i)
