from itertools import product

ans = []
for p in range(5):
    for v in "0123456789":
        for z in product("0123456789", repeat=p):
            z = "".join(z)
            n = int("12" + z + "34" + v + "5")
            if n <= 10 ** 8:
                if n % 2025 == 0:
                    ans.append([n, n // 2025])

for i in sorted(ans):
    print(*i)
