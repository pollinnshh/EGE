def f(x, s):
    if x >= 100: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 7, s - 1), f(x * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print()