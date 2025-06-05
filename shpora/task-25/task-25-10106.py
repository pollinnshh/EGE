from itertools import product

ans = []
for p in range(5):
    for v in "0123456789":
        for z in product("0123456789", repeat=p):
            z = "".join(z)
            n = int("1" + v + "2157" + z + "4")
            if n <= 10 ** 10:
                if n % 2024 == 0:
                    ans.append([n, n // 2024])

for i in sorted(ans):
    print(*i)
