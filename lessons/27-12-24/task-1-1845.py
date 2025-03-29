from itertools import permutations
grapf = "AB BV AV BG GD VD DZ ZE GE".split()
matrix = "67 567 456 35 234 123 12".split()
print(*range(1,8))
for i in permutations("ABVGDEZ"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in grapf):
        print(*i)