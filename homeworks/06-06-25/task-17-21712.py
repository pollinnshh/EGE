with open("17_21712.txt") as file:
    nums = [int(i) for i in file]

ans = []
min_ = min(i for i in nums if i > 0 and len(str(i)) == 4 and str(i)[-1] == "6")
for i in range(len(nums) - 2):
    n1, n2, n3 = nums[i:i + 3]
    u1 = len(str(abs(n1))) == 4 and str(n1)[-1] == "6"
    u2 = len(str(abs(n2))) == 4 and str(n2)[-1] == "6"
    u3 = len(str(abs(n3))) == 4 and str(n3)[-1] == "6"
    u4 = (n1 + n2 + n3) <= min_
    if (u1 + u2 + u3) == 1 and u4:
        ans.append(n1 + n2 + n3)
print(len(ans), max(ans))
