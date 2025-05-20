from itertools import *


def f(x):
    p = 257 <= x <= 10000
    r = 99 <= x <= 258
    q = 5 <= x <= 100
    a = a1 <= x <= a2
    return (a <= r) and (not (a <= p)) <= q


ans = []
line = [x for x in range(5, 1000)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(min(ans))
