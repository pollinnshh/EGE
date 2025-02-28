from fnmatch import fnmatch

ans = []
for i in range(1234, 10**10, 1234):
    if fnmatch(str(i), "4*5*6"):
        if i % 1234 == 0:
            ans.append([i, i // 1234])