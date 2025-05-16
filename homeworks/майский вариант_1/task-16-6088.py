from sys import setrecursionlimit


def f(n):
    if n > 3000: return 1
    if n <= 3000 and n % 2 == 0: return f(n + 1) - n + 1
    if n <= 3000 and n % 2 == 1: return f(n + 2) - 2 * n + 2


setrecursionlimit(345678)

print(2 * f(39) - 2 * f(34))
