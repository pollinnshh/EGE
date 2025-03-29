with open("17 (2)_7718.txt") as file:
    nums = [int(i) for i in file]

ans = []
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        n1, n2 = nums[i], nums[j]
        u1 = (n1 + n2) % 18 == 0
        u2 = (n1 * n2) % 18 == 0
        if u1 + u2 == 1:
            ans.append(n1 + n2)
print(len(ans), max(ans))

#data = [1, 2, 3, 4]
#for n1, n2 in combinations(data, r:2):

