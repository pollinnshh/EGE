from itertools import *

alf = "012345678"
cnt = 0
for val in product(alf,repeat=5):
    val = "".join(val)
    if val[0] != "0":
        if val.count("0") == 1 and "01" not in val and "03" not in val and "05" not in val and "07" not in val\
                and "10" not in val and "30" not in val and "50" not in val and "70" not in val:
            cnt += 1
print(cnt)