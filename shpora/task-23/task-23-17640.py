def f(x, end):
    if x < end:
        return False
    if x == end:
        return True
    return f(x - 2, end) + f(x // 2, end)


print(f(32, 14) * f(14, 1))
