from itertools import *

alf = sorted("цапля")
for pos, val in enumerate(product(alf, repeat=5), 1):
    val = "".join(val)
    if val.count("а") <= 1 and val.count("ц") == 2 and val.count("л") == 0:
        print(pos)
        break
