from itertools import *

alf = "ясновидец"
count = 0
for val in product(alf, repeat=5):
    u1 = val[0] in "снвдц"
    u2 = val[-1] in "яоие"
    u3 = val.count(val[0]) == 1
    u4 = val.count(val[-1]) == 1
    if u1 and u2 and u3 and u4:
        count += 1
print(count)
