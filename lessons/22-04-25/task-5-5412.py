for n in range(1, 10000):
    n1 = hex(n)[2:]
    if len(n1) % 2 == 0:
        n1 = "1" + n1
    else:
        n1 = n1 + "1"

    r = int(n1, 16)
    if 10 <= r <= 99:
        print(n)
