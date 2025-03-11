from string import digits, ascii_lowercase
alf = digits + ascii_lowercase
for x in alf[:22]:
    n1 = int("a23" + x + "ac0",22)
    n2 = int("gb" + x + "21670",22)
    if (n1 + n2) % 21 == 0:
        print((n1 + n2) // 22)