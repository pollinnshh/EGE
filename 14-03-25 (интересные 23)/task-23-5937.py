def f(x, end, cnt=0):
    if x % 2 == 0:
        cnt += 1
    if x > end:
        return 0
    if x == end and cnt <= 15:
        return 1
    return f(x + 2, end, cnt) + f(x + 3, end, cnt) + f(x * 2 + 1, end, cnt)


print(f(1, 55))
