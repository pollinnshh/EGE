from string import ascii_uppercase

alf = "0123456789" + ascii_uppercase
for x in alf[:23]:
    n1 = int(f"7{x}38596", 23)
    n2 = int(f"14{x}36", 23)
    n3 = int(f"61{x}7", 23)
    if (n1 + n2 + n3) % 22 == 0:
        print((n1 + n2 + n3) // 22)
