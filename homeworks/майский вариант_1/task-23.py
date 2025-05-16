def f(x, end):
    if x < end: return False
    if x == 15: return False
    if x == end: return True
    return f(x - 2, end) + f(x - 3, end) + f(x // 3, end)


print(f(17, 4) * f(25, 17) * f(48, 25))
