for n in range(1, 1000):
    n1 = bin(n)[2:]
    n2 = ""
    for i in n1:
        if i == "0":
            n2 += "1"
        if i == "1":
            n2 += "0"
    n2 = "1" + n2
    if n2.count("1") % 2:
        n2 = n2 + "1"
    else:
        n2 = n2 + "0"
    r = int(n2, 2)
    if r > 180:
        print(n)
        break
