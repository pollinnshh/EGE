from sys import setrecursionlimit


def f(n):
    if n <= 5:
        return 1
    else:
        return n + f(n - 2)


setrecursionlimit(45678)
print(f(2126) - f(2122))
