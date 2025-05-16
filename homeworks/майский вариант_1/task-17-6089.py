def f(num):
    res = []
    for i in range(1, int(num * 0.5) + 1):
        if num % i == 0:
            res.append(i)
            res.append(num // i)
    res = sorted(set(res))
    return res


with open("17_6089.txt") as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if str(i)[-1] == "2")

ans = []
for i in data:
    if abs(i) % 3 == 0 and abs(i) % 7 and abs(i) % 17:
        if abs(i) in f(maxx):
            ans.append(i)

print(len(ans), max(ans))
