from string import digits, ascii_lowercase
alf = digits + ascii_lowercase
for x in alf[:25]:
    n1 = int("11353" + x + "12", 25)
    n2 = int("135" + x + "21", 25)
    num = n1 + n2
    if num % 24 == 0:
        print(x, num // 24)