ans = []
for x in range(1, 2030):
    n = 7 ** 170 + 7 ** 100 - x
    cnt = 0
    while n:
        if n % 7 == 0:
            cnt += 1
        n //= 7
    ans.append([cnt, x])

print(max(ans))
