from functools import lru_cache

@lru_cache(None)
def f(x, end):
    if x == end:
        return 1
    if x < -50 or x > 50:
        return 0
    if len(ans) != len(set(ans)):
        return 0
    return f(x + 2, end) + f(x - 3, end)

print(f(1, 30))