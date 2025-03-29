for n in range(100, 1000):
    n1 = sorted(int(i) for i in str(n))
    min_ch = str(n1[0]) + str(n1[1])
    max_ch = str(n1[2]) + str(n1[1])
    if min_ch[0] == "0":
        min_ch = str(n1[1]) + str(n1[0])
    r = int(max_ch) - int(min_ch)
    if r == 63:
        print(n)
        break
