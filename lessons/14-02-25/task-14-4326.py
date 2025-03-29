num = 3*15**1140 + 2*15**1025 + 15**923 - 3*15**85 + 2*15**74 + 3
count = 1
ans = 0
while num:
    if num % 15 == (num // 15) % 15:
        count += 1
    else:
        ans = max(ans,count)
        count = 1
    num //= 15
print(ans)