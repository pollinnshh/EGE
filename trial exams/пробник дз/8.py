from itertools import product
from string import digits, ascii_lowercase
alf = digits + ascii_lowercase
count = 0
for val in product(alf[:12], repeat=7):
    val = "".join(val)
    chet = "02468a"
    nechet = "13579b"
    if val[0] != "0":
        u1 = val.count("b") == 2
        val1 = val.replace("4", "2").replace("8", "2").replace("a", "2").replace("0", "2").replace("6", "2")\
            .replace("3", "1").replace("5", "1").replace("7", "1").replace("9", "1").replace("b", "1")
        u2 = "11" not in val1 and "22" not in val1
        if u1 and u2:
            count += 1
print(count)

