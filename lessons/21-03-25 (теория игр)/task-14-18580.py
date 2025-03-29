from string import ascii_lowercase, digits

alf = digits + ascii_lowercase

ans = []
for x in alf[:25]:
    n1 = int("a4" + x + "7f2", 25)
    n2 = int("n" + x + "g5" + x + "h", 25)
    n3 = int("74" + x + "m26", 25)
    if (n1 + n2 + n3) % 24 == 0:
        ans.append([x, (n1 + n2 + n3) // 24])
print(sorted(ans)[::-1])
