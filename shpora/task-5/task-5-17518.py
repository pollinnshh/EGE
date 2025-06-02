for n in range(1, 10000):
    n1 = bin(n)[2:]
    if n1.count("1") % 2 == 0:
        n1 = "10" + n1[2:] + "0"
    elif n1.count("1") % 2 == 1:
        n1 = "11" + n1[2:] + "1"

    r = int(n1, 2)
    if r > 50:
        print(n)
        break
