ans = []
for x in range(1, 3000):
    n = 4 ** 210 + 4 ** 110 - x
    cnt = 0
    while n:
        if n % 4 == 0:
            cnt += 1
        n //= 4
    ans.append([cnt, x])
print(sorted(ans, key=lambda x: (-x[0], x[1])))
