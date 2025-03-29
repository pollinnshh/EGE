
def f(n):
    if n > 3000:
        return n
    if n % 2 == 0 and n <= 3000:
        return n + f(n + 1) + 1
    if n % 2 != 0 and n <= 3000:
        return f(n + 2) + 2
print(f(40) - f(43))