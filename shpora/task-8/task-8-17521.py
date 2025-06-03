from itertools import *

alf = "01234567"
cnt = 0
for val in product(alf, repeat=5):
    val = "".join(val)
    if val[0] != "0":
        if val[0] not in "1357" and val[-1] not in "26" and val.count("7") <= 2:
            cnt += 1

print(cnt)
