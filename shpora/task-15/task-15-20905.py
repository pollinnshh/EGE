from itertools import combinations


def f(x):
    p = 17 <= x <= 58
    q = 29 <= x <= 80
    a = a1 <= x <= a2
    return p <= ((q and (not a)) <= (not p))


ans = []
line = [x + eps for x in range(16, 80) for eps in [0, 0.1, 0.9]]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)

print(min(ans))
