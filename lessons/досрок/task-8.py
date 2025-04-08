from itertools import *

cnt = 0
alf = "дгиашэ"
for val in product(alf, repeat=5):
    val = "".join(val)
    if val[0] not in "иаэ" and val[-1] not in "дшг":
        cnt += 1
print(cnt)
