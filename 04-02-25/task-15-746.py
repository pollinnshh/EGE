from itertools import combinations


def f(x):
    p = 12 <= x <= 26
    q = 30 <= x <= 53
    a = a1 <= x <= a2
    return (a <= p) or q


ans = []
line = [x / 10 for x in range(11 * 10, 55 * 10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(max(ans))
