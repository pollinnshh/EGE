def prosto(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1


for n in range(4, 1000):
    st = ">" + "0" * 25 + "1" * n + "2" * 25
    while ">1" in st or ">2" in st or ">0" in st:
        st = st.replace(">1", "22>", 1)
        st = st.replace(">2", "2>",1)
        st = st.replace(">0", "1>", 1)
    summ = sum(map(int, st[:-1]))
    if prosto(summ):
        print(n)
