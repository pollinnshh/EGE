from itertools import combinations


def f(x):
    b = 80 <= x <= 100
    a = a1 <= x <= a2
    return ((x % 17) == 0) <= ((not b) or (a < (x + 30)))


ans = []
line = [x / 10 for x in range(60 * 10, 115 * 10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(max(ans))