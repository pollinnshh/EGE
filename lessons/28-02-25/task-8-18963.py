from itertools import *

count = 0
alf = "котбус"
for val in product(alf, repeat=8):
    val = "".join(val)
    if "кот" in val and val[0] not in "оу":
        count += 1
print(count)
