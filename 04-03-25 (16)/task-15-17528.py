from itertools import combinations


def f(x):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2
    return p <= ((q and (not a)) <= (not p))


line = [x / 10 for x in range(15 * 10, 64 * 10)]
ans = []
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(min(ans))
