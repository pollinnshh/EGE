from itertools import *


def f(x):
    p = 254 <= x <= 800
    q = 410 <= x <= 823
    a = a1 <= x <= a2
    return (p and (not a)) <= q


ans = []
line = [x / 2 for x in range(254 * 2, 825 * 2)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(min(ans))
