with open("input.txt") as file:
    data = file.readline()

posA = [i for i in range(len(data)) if data[i] == "A"]

countA = len(posA) - 1
ans = 0
for i in range(len(posA) - 1):
    if posA[i + 1] - posA[i] > 1:
        ans += countA
    else:
        ans += countA - 1
    countA -= 1
print(ans)
