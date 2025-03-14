def f(x, end, b=0):
    if x == end:
        return 1
    if x > end:
        return 0
    if b == 0:
        return f(x + 2, end) + f(x ** 2, end, 1) + f(x * 3, end)
    return f(x + 2, end) + f(x * 3, end)

print(f(2, 64))