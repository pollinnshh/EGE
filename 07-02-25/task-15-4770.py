from itertools import *
def f(a):
    p = 35 <= x <= 55
    q = 45 <= x <= 65
    a = a1 <= x <= a2
    return (p <= a) and ((not a) <= (not q))
ans = []
line = [x / 10 for x in range(33 * 10, 67 * 10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2 - a1)
print(min(ans))
