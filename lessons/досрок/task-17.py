with open("17.txt") as file:
    nums = [int(i) for i in file]

otr = sum(i for i in nums if i < 0)

ans = []
for i in range(len(nums) - 2):
    n1, n2, n3 = nums[i: i + 3]
    u1 = max(n1, n2, n3) * min(n1, n2, n3) > otr
    if u1:
        ans.append(n1 + n2 + n3)

print(len(ans), abs(max(ans)))
