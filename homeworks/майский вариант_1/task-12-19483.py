for n in range(4, 10000):
    t = "2" + n * "5"
    while "25" in t or "355" in t or "555" in t:
        t = t.replace("25", "5", 1)
        t = t.replace("355", "522", 1)
        t = t.replace("555", "3", 1)
    if t.count("2") == 10:
        print(n)
        break
