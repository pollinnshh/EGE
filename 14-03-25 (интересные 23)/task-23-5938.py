def f(x, end, cnt=0):
    if x > end:
        return 0
    if x == end and cnt == 51:
        return 1
    return f(x * 4, end, cnt + 1) + f(x + 1, end, cnt + 1) + f(x * 3, end, cnt + 1)


print(f(2, 404))
