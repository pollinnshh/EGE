def f(x, end, a=0, b=0, c=0):
    if x > end:
        return 0
    if x == end and a <= 4 and b >= 2 and c == 5:
        return 1
    return f(x * 5, end, a + 1, b, c) + f(x * 3, end, a, b + 1, c) + f(x + 45, end, a, b, c + 1)


print(f(1, 2970))
