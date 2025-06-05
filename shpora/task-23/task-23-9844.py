def f(x, end):
    if x < end:
        return False
    if x == end:
        return True
    if x == 7:
        return False
    return f(x - 1, end) + f(x - 3, end) + f(x // 2, end)


print(f(19, 10) * f(10, 3))
