from itertools import product
alf = "ABCDEF"
count = 0
for val in product(alf, repeat = 6):
    val = "".join(val)
    val1 = val.replace("A", "E")
    if val1[0] != "E" and val1[-1] != "E":
        count += 1
print(count)