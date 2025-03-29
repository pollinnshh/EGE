from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)


for i in range(2060):
    f(i)

print((2 * f(2024) + f(2023)) // f(2022))
