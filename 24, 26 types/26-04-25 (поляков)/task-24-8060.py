from re import *

with open("24-333.txt") as file:
    data = file.readline()

pattern = r"(yandex.ru|gmail.com)*[a-zA-Z0-9.]+[a-zA-Z0-9][@](yandex.ru|gmail.com)"
matches = finditer(pattern, data)
print(len(max([i.group() for i in matches], key=len)))
 