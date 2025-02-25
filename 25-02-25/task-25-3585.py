from fnmatch import fnmatch

for i in range(123405708 - 123405708 % 17, 10 ** 10,17):
    if fnmatch(str(i), "1234?57?8"):
        if i % 17 == 0:
            print(i, i // 17)