with open("17_17680.txt") as file:
    nums = [int(i) for i in file]

ans = []
min_ = min(i for i in nums if i > 0 and i % 41 == 0)
for i in range(len(nums) - 1):
    n1, n2 = nums[i], nums[i + 1]
    u1 = n1 != n2
    u2 = abs(n2 - n1) % min_ == 0
    if u1 + u2 == 2:
        ans.append(n1 + n2)

print(len(ans), max(ans))