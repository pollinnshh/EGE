from fnmatch import fnmatch

for i in range(21025, 10**10, 21025):
    if fnmatch(str(i), "12*34?5"):
        stri = str(i)
        u = stri.count("0") + stri.count("2") + stri.count("4") + stri.count("6") + stri.count("8") == \
            stri.count("1") + stri.count("3") + stri.count("5") + stri.count("7") + stri.count("9")
        if i % 21025 == 0 and u:
            print(i, i // 21025)