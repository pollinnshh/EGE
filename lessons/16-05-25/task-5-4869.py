for n in range(1, 10000):
    n1 = bin(n)[2:]
    cnt_1 = len([i for i in n1[1::2] if i == "1"])
    cnt_0 = len([i for i in n1[::2] if i == "0"])
    r = abs(cnt_0 - cnt_1)
    if r == 5:
        print(n)
        break
