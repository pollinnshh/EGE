from fnmatch import *

for i in range(7993, 10 ** 10, 7993):
    if fnmatch(str(i), "4*4736*1"):
        if i % 7993 == 0:
            print(i, i // 7993)
