with open("1706.txt") as file:
    nums = [int(i) for i in file]

ans = []
min_ch = min(i for i in nums if len(str(abs(i))) == 3 and str(i)[-2:] == "19")
for i in range(len(nums) - 2):
    n1, n2, n3 = nums[i:i + 3]
    u1 = str(n1)[-2:] == "19" and len(str(abs(n1))) == 5
    u2 = str(n2)[-2:] == "19" and len(str(abs(n2))) == 5
    u3 = str(n3)[-2:] == "19" and len(str(abs(n3))) == 5
    if u1 + u2 + u3 >= 1 and (n1 + n2 + n3) > min_ch ** 2:
        ans.append(n1 + n2 + n3)
print(len(ans), min(ans))
