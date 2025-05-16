ans = []
alf = "0123456789ABCDEF"
for x in alf:
    for y in alf:
        n1 = int(f"27A{x}23", 16)
        n2 = int(f"8{y}E5D2", 16)
        if (n1 + n2) % 5 == 0:
            ans.append(int(x, 16) + int(y, 16))

print(max(ans))