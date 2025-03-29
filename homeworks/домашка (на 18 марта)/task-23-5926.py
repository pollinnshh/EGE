def f(x, cnt=0, a=0, b=0, c=0):
    if cnt < 24:
        return []
    if cnt == 24:
        return [x]
    return f(x + 1, cnt + 1, a + 1) + f(x + 7, cnt + 1, b + 1) + f(x * 4, cnt + 1, c + 1)

print(len(set(f(1))))