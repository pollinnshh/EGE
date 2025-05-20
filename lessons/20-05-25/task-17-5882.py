with open("17_5882.txt") as file:
    nums = [int(i) for i in file]

ans = []
for i in range(len(nums) - 1):
    n1, n2 = nums[i], nums[i + 1]
    u1 = str(n1)[-1] == "3"
    u2 = str(n2)[-1] == "3"
    if u1 + u2 == 1:
        if n1 < n2:
            ans.append(n1)
        else:
            ans.append(n2)

m = str(abs(min(ans)))
n = sum(int(i) ** 2 for i in m)
res = []
for num in nums:
    if "3" in str(num):
        if num >= n:
            res.append(num)

print(len(res), min(res))
