def f(x, end):
    if x > end:
        return 0
    if x == 16:
        return 0
    if x == end:
        return 1
    return f(x + 2, end)+ f(x * 2, end) + f(x * 3,end)

print(f(13,45))