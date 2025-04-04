def f1(arr):
    return max(arr) < sum(arr) - max(arr)


def f2(arr):
    return len(set(arr)) + 1 == len(arr)


# def f2(arr):
#     cnt = [arr.count(i) for i in arr]
#     return cnt.count(2) == 2 and cnt.count(1) == 2


with open("9_4614.txt") as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)
