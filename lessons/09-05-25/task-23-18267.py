def f(x, end, c=0):
    if x == end and c != 1:
        return True
    if x > end:
        return False
    return f(x + 2, end) + f(x + 5, end) + f(x ** 2, end, c=1)


print(f(4, 36))
