from itertools import *

alf = sorted("парижанка")
for val in set(permutations(alf)):
    val = "".join(val)
    val = val.replace("и", "а")
    