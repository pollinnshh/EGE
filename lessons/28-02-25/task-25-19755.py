def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i): res.add(i)
            if is_prime(num // i): res.add(num // i)

    if len(res) <= 1:
        return 0

    m = max(res) + min(res)
    if m > 2000 and str(m)[-1] == "8":
        return m
    return 0

count = 0
for i in range(1_200_001, 10 ** 20):
    res = f(i)
    if res:
        print(i, res)
        count +=  1
        if count == 5:
            break
