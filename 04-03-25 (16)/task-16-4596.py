def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2:
        return f(n - 2) + 2 * n - 2
    return f(n - 1) + n - 1


print(f(34))
