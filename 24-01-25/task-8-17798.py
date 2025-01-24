from itertools import product
alf = sorted("минус")
for pos, val in enumerate(product(alf,repeat=4),1):
    val = "".join(val)
    if val.count("и") + val.count("у") <= val.count("м") + val.count("н") + val.count("с"):
        print(pos)

