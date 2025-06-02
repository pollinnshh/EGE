from itertools import permutations

matrix = '68 47 45 237 368 15 248 157 '.split()
graph = 'AC CE EG GF FA AB BF EH HD DC'.split()

print(*range(1, 9))  # количество столбцов в матрице
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
