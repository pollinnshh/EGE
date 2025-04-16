from sys import setrecursionlimit


def f(n):
    if n >= 10000: return n
    if n < 10000 and n % 2 == 0: return f(n + 1) + n ** 2 - 3 * (n - 1)
    if n < 10000 and n % 2: return f(n + 2) + 5 * n - (n - 1)


setrecursionlimit(2345678)

print(f(90) - f(99))
