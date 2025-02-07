from itertools import combinations


def f(x):
    p = 25 <= x <= 73
    q = 75 <= x <= 118
    a = a1 <= x <= a2
    return (a and (not q)) <= (p or q)


ans = []
line = [x / 10 for x in range(23 * 10, 120 * 10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(max(ans))
