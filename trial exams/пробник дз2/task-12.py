for n in range(4, 10000):
    st = '5' + '2' * n
    while '52' in st or '2222' in st or '1122' in st:
        st = st.replace('52', '11', 1)
        st = st.replace('2222', '5', 1)
        st = st.replace('1122', '25', 1)
    if str(sum(map(int, st)))[-1] == "7":
        print(n, st, sum(map(int, st)))
        break