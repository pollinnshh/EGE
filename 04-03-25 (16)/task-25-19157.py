from fnmatch import fnmatch

for i in range(6437, 10 ** 10, 6437):
    if fnmatch(str(i), "1?3*5*954"):
        if i % 6437 == 0:
            print(i, i // 6437)
