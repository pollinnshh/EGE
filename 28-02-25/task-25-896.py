def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


count = 0
for i in range(194441, 196501):
    if str(i)[-2:] == "93" and is_prime(i):
        count += 1
        print(count, i)
