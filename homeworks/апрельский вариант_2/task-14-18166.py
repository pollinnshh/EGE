ans = []
for x in range(2, 2026):
    cnt = 0
    num = 5 ** 2025 + 5 ** 200 - x
    while num:
        if num % 5 == 4:
            cnt += 1
        num //= 5
    ans.append([cnt, x])

print(max(ans))
