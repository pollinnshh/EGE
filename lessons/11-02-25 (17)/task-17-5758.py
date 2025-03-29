with open("17_5758.txt") as file:
    data = [int(i) for i in file]

s = set(data)
count = 0
moda = 0
for i in s:
    if count < data.count(i):
        count = data.count(i)
        moda = i
ans = []
for i in range(len(data)):
    for j in range(i + 2, len(data), 2):
        if data[i] < moda < data[j] or data[i] > moda > data[j]:
            ans.append(max(abs(moda - data[i]), abs(moda - data[j])))
print(len(ans), max(ans))