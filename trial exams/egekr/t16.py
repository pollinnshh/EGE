from sys import setrecursionlimit


def f(n):
    if n < 20:
        return n
    else:
        return (n - 6) * f(n - 7)


setrecursionlimit(34567)
print((f(47872) - 290 * f(47865)) // f(47858))
