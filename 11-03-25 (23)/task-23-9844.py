def f(x, end):
    if x == 7:
        return 0
    if x < end:
        return 0
    if x == end:
        return 1
    return f(x - 1, end) + f(x - 3, end) + f(x // 2, end)
print(f(19, 10) * f(10, 3))