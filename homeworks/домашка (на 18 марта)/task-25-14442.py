from fnmatch import *

ans = []
for i in range(70, 10000):
    if fnmatch(str(i), "*7?"):
        for n in range(400000, 500001):
            if n % i == 0:
                ans.append(i)
                if len(ans) == 18:
                    print(n, sum(ans))