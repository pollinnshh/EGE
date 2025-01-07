ans = []
for x in range(1,5556)[::-1]:
    n = 5**150 + 5**135 - x
    count = 0
    while n:
        if n % 5 == 4:
            count += 1
        n //= 5
        if count == 134:
            ans.append(int(x))
print(max(ans))