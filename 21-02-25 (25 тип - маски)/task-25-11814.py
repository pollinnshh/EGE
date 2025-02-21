from fnmatch import fnmatch

for i in range(1777, 10 ** 10, 1777):
    if fnmatch(str(i), "21???68?79"):
        if i % 1777 == 0:
            print(i, i // 1777)