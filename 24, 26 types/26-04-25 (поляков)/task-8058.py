from re import *

with open("24-332.txt") as file:
    data = file.readline()

pattern = r"([ABC][abc]*[ ])(([ABC]|[abc])[abc]*[ ])+[abc][.]"
matches = finditer(pattern, data)
match = [i.group() for i in matches]

# ans = []
# for i in match:
#    if "  " not in i:
#        ans.append(len(i))

print(len(max(match, key=len)))
