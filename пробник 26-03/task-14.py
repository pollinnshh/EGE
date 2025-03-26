ans = []
for x in range(1, 2031):
    num = 2 ** 2025 + 2 ** 2024 - 2 ** 2021 - x
    count = 0
    while num:
        if num % 4 == 0:
            count += 1
        num //= 4
    ans.append([count, x])
print(sorted(ans)[::-1])
