from string import ascii_lowercase

def conv(num, sys):
    res = ""
    alf = "0123456789" + ascii_lowercase
    while num:
        res += alf[num % sys]
        num //= sys
    return res[::-1]

for n in range(1,10000):
    n1 = conv(n, 12)
    if n % 3 == 0:
        n1 = "1" + n1 + "b"
    else:
        n1 = "2" + n1 + "0"
    r = int(n1, 12)
    if r < 1996:
        print(r)