def f(x, end):
    if x == end:
        return 1
    if x < end:
        return 0
    return f(x - 3, end) + f(x // 3, end)
print(f(35, 8)  * f(8, 1))