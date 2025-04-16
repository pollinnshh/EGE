def f(x, s, u=0):
    if x > 40: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 3, s - 1, u=3), f(x + 6, s - 1, u=6), f(x * 2, s - 1, u=2)]
    if u == 3:
        h = [f(x + 6, s - 1, u=6), f(x * 2, s - 1, u=2)]
    elif u == 6:
        h = [f(x + 3, s - 1, u=3), f(x * 2, s - 1, u=2)]
    elif u == 2:
        h = [f(x + 3, s - 1, u=3), f(x + 6, s - 1, u=6)]
    return any(h) if (s - 1) % 2 == 0 else all(h)


print("19)", [s for s in range(2, 37) if f(s, 2)])
print("20)", [s for s in range(2, 37) if not f(s, 1) and f(s, 3)])
print("21)", [s for s in range(2, 37) if not f(s, 2) and f(s, 4)])
