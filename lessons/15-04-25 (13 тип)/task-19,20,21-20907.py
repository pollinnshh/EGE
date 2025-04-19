def f(x1, x2, s):
    if x1 + x2 >= 81: return s % 2 == 0
    if s == 0: return False
    h = [f(x1 + 1, x2, s - 1), f(x1, x2 + 1, s - 1), f(x1 * 2, x2, s - 1), f(x1, x2 * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)


print("19)", [s for s in range(1, 74) if f(7, s, 2)])
print("20)", [s for s in range(1, 74) if not f(7, s, 1) and f(7, s, 3)])
print("21)", [s for s in range(1, 74) if not f(7, s, 2) and f(7, s, 4)])
