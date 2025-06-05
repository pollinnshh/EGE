with open("17_17636.txt") as file:
    nums = [int(i) for i in file]

ans = []
max_ = max(i for i in nums if str(i)[-1] == "3" and len(str(abs(i))) == 3)
for i in range(len(nums) - 2):
    n1, n2, n3 = nums[i], nums[i + 1], nums[i + 2]
    u1 = len(str(abs(n1))) == 3 and str(n1)[-1] == "3"
    u2 = len(str(abs(n2))) == 3 and str(n2)[-1] == "3"
    u3 = len(str(abs(n3))) == 3 and str(n3)[-1] == "3"
    u4 = (n1 + n2 + n3) < max_
    if (u1 + u2 + u3) >= 1 and u4:
        ans.append(n1 + n2 + n3)

print(len(ans), max(ans))
