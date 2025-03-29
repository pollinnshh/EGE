def f(x, end):
    if x == end:
        return 1
    if int(x) > int(end):
        return 0
    return f(x + "0", end) + f(str(int(x) + 1), end) + f(x + "1", end)

print(f("100", "11101"))