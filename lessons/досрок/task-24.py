from string import *

alf = ascii_uppercase[2:]
with open("") as file:
    data = file.readline()

for i in alf:
    st = data.replace(i, " ")

st = data.split()

for i in data:
    i = i.rstrip("13579B").lstrip("0")

print(len(max(data, key=len)))
