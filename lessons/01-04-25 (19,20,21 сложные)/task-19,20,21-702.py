def f(x, s):
    if x >= 36:
        if x <= 85: return s % 2 == 0
        else: return s % 2 != 0
    if s == 0: return 0
    h = [f(x + 2, s - 1), f(x * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print("19)", f(30, 3), f(32, 3))
print("20)", f(8, 9), f(10, 9))
print("21)", f(6, 21))