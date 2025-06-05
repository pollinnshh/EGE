with open("17_17558.txt") as file:
    nums = [int(i) for i in file]

ans = []
x = len([i for i in nums if abs(i) % 32 == 0])
for i in range(len(nums) - 1):
    n1, n2 = nums[i], nums[i + 1]
    u1 = n1 < 0
    u2 = n2 < 0
    u3 = (n1 + n2) < x
    if u1 + u2 >= 1 and u3:
        ans.append(n1 + n2)

print(len(ans), max(ans))
