from itertools import product
from string import digits, ascii_lowercase
alf  = digits + ascii_lowercase
nechet = "13579bdfhjln"
count = 0
for val in product(alf[:25],repeat = 4):
    val = "".join(val)
    if val[0] != "0":
        u1 = (val[0] in nechet) + (val[1] in nechet) + (val[2] in nechet) + (val[3] in nechet) == 1
        u2 = val.count("0") + val.count("1") + val.count("2") + val.count("3") + val.count("4") + val.count("5") <= 2
        if u1 and u2:
            count += 1
print(count)