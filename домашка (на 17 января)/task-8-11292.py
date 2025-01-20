from itertools import product
from string import digits, ascii_lowercase

alf = digits + ascii_lowercase
count = 0
for n in product(alf[:16], repeat=5):
    n = "".join(n)
    if n[0] != "0":
        u1 = n.count("6") == 2
        n1 = n.replace("4", "2").replace("8", "2").replace("a", "2") \
            .replace("c", "2").replace("e", "2").replace("0", "2")
        u2 = "26" not in n1 and "62" not in n1 and "66" not in n1
        if u1 and u2:
            count += 1
print(count)
