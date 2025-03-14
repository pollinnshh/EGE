def f(x, end, a=0):
    if x > end + 1:
        return 0
    if x == end:
        return 1
    if a == 0:
        return f(x - 1, end, 1) + f(x * 2, end) + f(x * 3, end)
    return f(x * 2, end) + f(x * 3, end)


print(f(3, 15))
