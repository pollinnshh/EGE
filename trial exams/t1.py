from itertools import *

matrix = "26 134678 27 257 48 128 234 256".split()
graph = "ВА АГ ГБ БД ДИ ИЖ ЖЕ ЕВ ВГ ГЕ ГД ГИ".split()
print(*range(1, 9))

for i in permutations("АБВГДЕЖИ"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
