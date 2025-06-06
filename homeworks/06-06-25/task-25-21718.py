# from itertools import product
#
# ans = []
# for p in range(6):
#     for z1 in product("0123456789", repeat=p):
#         for z2 in product("0123456789", repeat=p):
#             z1 = "".join(z1)
#             z2 = "".join(z2)
#             n = int("4" + z1 + "4736" + z2 + "1")
#             if n <= 10 ** 10:
#                 if n % 7993 == 0:
#                     ans.append([n, n // 7993])
#
# for i in sorted(ans):
#     print(*i)

from fnmatch import *

for i in range(7993, 10 ** 10, 7993):
    if fnmatch(str(i), "4*4736*1"):
        if i % 7993 == 0:
            print(i, i // 7993)
