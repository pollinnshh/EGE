def f(x1, x2, s):
    if x1 + x2 >= 175: return s % 2 == 0
    if s == 0: return 0
    h = [f(x1 + 1, x2, s - 1), f(x1 * 3, x2, s - 1), f(x1, x2 + 1, s - 1), f(x1, x2 * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)


print("19)", [s for s in range(1, 155) if f(19, s, 2)])
print("20)", [s for s in range(1, 155) if not f(19, s, 1) and f(19, s, 3)])
print("21)", [s for s in range(1, 155) if not f(19, s, 2) and f(19, s, 4)])
