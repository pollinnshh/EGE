def f(x, cnt=0):
    if cnt == 13 and x < 0:
        return [x]
    if cnt > 13:
        return []
    return f(x - 3, cnt + 1) + f(x * (-3), cnt + 1)


print(len(set(f(333))))
