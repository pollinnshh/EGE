from sys import setrecursionlimit


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)


setrecursionlimit(456789)
print((2 * f(2024) + f(2023)) // f(2022))
