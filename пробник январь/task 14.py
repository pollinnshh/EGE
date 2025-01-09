from string import digits, ascii_lowercase
alf = digits + ascii_lowercase
for x in alf[:26]:
    n1 = int("27" + x + "98876", 26)
    n2 = int("26" + x + "51", 26)
    n3 = int("15" + x + "47", 26)
    n4 = int("62" + x + "5", 26)
    num = n1 + n2 + n3 + n4
    if num % 25 == 0:
        print(x, num // 25)
