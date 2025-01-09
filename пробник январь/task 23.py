def f(x, end):
    if x > end:
        return 0
    if x == 16:
        return 0
    while x != end:
        return x + 2 + x * 2 + x * 3

print(f(13,45))