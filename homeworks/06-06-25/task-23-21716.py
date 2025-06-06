def f(x, end):
    if x > end: return False
    if x == 56: return False
    if x == end: return True
    return f(x + 3, end) + f(x + 7, end) + f(x * 3, end)


print(f(12, 40) * f(40, 72) * f(72, 89))
