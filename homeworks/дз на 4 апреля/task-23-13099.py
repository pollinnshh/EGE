def f(x, end, a=0):
    if x == end: return True
    if (x - 1) > end: return False
    if a == 1: return f(x * 2, end) + f(x * 3, end)
    return f(x - 1, end, a + 1) + f(x * 2, end) + f(x * 3, end)


print(f(3, 15))
