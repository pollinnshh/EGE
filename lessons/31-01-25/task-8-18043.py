from itertools import product
alf = "012345678"
count = 0
for val in product(alf, repeat=7):
    val = "".join(val)
    if (val[0] not in "0246") and val[-3:] not in "000 111 222 333 444 555 666 777 888":
        count += 1
print(count)
