def f(x, end):
    if x > end: return False
    if x == 35: return False
    if x == end: return True
    return f(x + 1, end) + f(x + 2, end) + f(x * 2, end)


print(f(7, 13) * f(13, 15) * f(15, 51))
