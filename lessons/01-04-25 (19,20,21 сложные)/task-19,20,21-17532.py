def f(x1, x2, s):
    if x1 + x2 >= 65: return (s % 2) == 0
    if s == 0: return 0
    h = [f(x1 + 1, x2, s - 1), f(x1, x2 + 1, s - 1), f(x1 * 3, x2, s - 1), f(x1, x2 * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print("19)", [s for s in range(1, 59) if f(6, s, 2)]) #any(h)
print("20)", [s for s in range(1, 59) if not f(6, s, 1) and f(6, s, 3)])
print("21)", [s for s in range(1, 59) if not f(6, s, 2) and f(6, s, 4)])

