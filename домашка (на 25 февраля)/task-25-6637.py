## 1
from fnmatch import fnmatch

for i in range(3052, 10 ** 10, 3052):
    if fnmatch(str(i), "1?2139*4"):
        if i % 3052 == 0:
            print(i, i // 3052)
