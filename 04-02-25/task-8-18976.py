from itertools import product
from string import digits, ascii_lowercase
alf = digits + ascii_lowercase
count = 0
for val in product(alf[:20],repeat=5):
    val = "".join(val)
    if val[0] != "0":
        if (int(val[0],20) + int(val[-1],20) == 26) and \
                (((int(val[0],20) + int(val[2],20) + int(val[4],20)) % 2 == 0 and (int(val[1],20) % 2 == 0 and int(val[3],20)) % 2 == 0) or ((int(val[0],20) + int(val[2],20) + int(val[4],20)) % 2 != 0 and (int(val[1],20) + int(val[3],20)) % 2 == 0)):
            count += 1
print(count)