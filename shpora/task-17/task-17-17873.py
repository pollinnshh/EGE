with open("17_17873.txt") as file:
    nums = [int(i) for i in file]

ans = []
min_ = min(nums)
for i in range(len(nums) - 1):
    n1, n2 = nums[i], nums[i + 1]
    u1 = n1 % 16 == min_
    u2 = n2 % 16 == min_
    if u1 + u2 >= 1:
        ans.append(n1 + n2)

print(len(ans), max(ans))
