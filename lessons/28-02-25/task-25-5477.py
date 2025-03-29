def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def f(num):
    res = list()
    if num % 6 == 0:
        if is_prime(num + 1) and is_prime(num - 1):
            res += [num + 1, num - 1]
    return res[::-1]


count = 0
for i in range(600_001, 10 ** 20):
    if f(i):
        print(*f(i))
        count += 1
        if count == 6:
            break
