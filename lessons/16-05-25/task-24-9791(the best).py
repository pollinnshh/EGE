from string import ascii_uppercase

with open("24_9791.txt") as file:
    data = file.readline()

for c in ascii_uppercase[6:]:
    data = data.replace(c, " ")

data = data.split()

ans = []
for i in data:
    s = i.lstrip("0")
    if int(s, 16) % 20 == 0:
        ans.append(s)
    else:
        for l in range(len(s)):
            for r in range(len(s) + 1, l, -1):
                ps = s[l:r]
                if int(ps, 16) % 20 == 0:
                    ans.append(ps)
                    break

print(len(max(ans, key=len)))
