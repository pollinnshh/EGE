def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    if x == 7:
        return f(x + 2, end) + f(x * 2, end)
    return f(x + 2, end) + f(x + 5, end) + f(x * 2, end)


print(f(7, 23) * f(23, 35))
