def f(x, end):
    if x < end:
        return 0
    if x == end:
        return 1
    return f(x - 1, end) + f(x // 2, end)

print(f(30, 12) * f(12, 1))
