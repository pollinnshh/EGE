def f(x, end):
    if x < end: return False
    if x == 9 or x == 16: return False
    if x == end: return True
    return f(x - 1, end) + f(x - 2, end) + f(x // 3, end)

print(f(19, 3))