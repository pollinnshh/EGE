def  f(x, end):
    if x == 9 or x == 16:
        return 0
    if x < end:
        return 0
    if x == end:
        return 1
    return f(x - 2, end) + f(x - 1, end) + f(x // 3, end)
print(f(19, 3))