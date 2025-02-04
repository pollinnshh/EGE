from itertools import combinations


def f(x):
    p = 43 <= x <= 49
    q = 44 <= x <= 53
    a = a1 <= x <= a2
    return (a <= p) or q


ans = []
line = [x / 10 for x in range(41 * 10, 55 * 10)]  # [30, 43, 44, 49, 53, 60]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):  # all(f(x / 10) for x in range(a1 * 10 - 1, a2 * 10 + 1))
        ans.append(a2 - a1)
print(max(ans))
