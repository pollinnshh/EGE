with open("17_21416.txt") as file:
    nums = [int(i) for i in file]

sum_ = sum(i for i in nums if i < 0)

ans = []
for i in range(len(nums) - 2):
    n1, n2, n3 = nums[i:i + 3]
    u1 = min(n1, n2, n3) * max(n1, n2, n3) > sum_
    if u1:
        ans.append(n1 + n2 + n3)

print(len(ans), max(ans))
