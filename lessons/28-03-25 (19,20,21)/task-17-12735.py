with open("17_12735.txt") as file:
    nums = [int(i) for i in file]

ans = []
max_el = max(i for i in nums if str(i)[-2:] == "09")
for i in range(len(nums) - 2):
    n1, n2, n3 = nums[i: i + 3]
    u1 = n1 % 7 == 0
    u2 = n2 % 7 == 0
    u3 = n3 % 7 == 0
    summ = n1 + n2 + n3
    if u1 + u2 + u3 == 2 and summ < max_el:
        ans.append(n1 * n2 * n3)
print(len(ans), min(ans))
