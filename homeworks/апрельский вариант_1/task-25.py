from itertools import product

for p in range(3):
    for v in '0123456789':
        for z in product("0123456789", repeat=p):
            z = "".join(z)
            st = int("12" + v + z + "45")
            ans = []
            for i in range(2, int(st ** 0.5) + 1):
                if st % i == 0:
                    ans.append(i)
                    ans.append(st // i)
            ans = sorted(set(ans))
            if len(ans) == 18:
                print(st, max(ans))
