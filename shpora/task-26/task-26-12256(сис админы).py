with open("26_12256.txt") as file:
    s, n = map(int, file.readline().split())
    boxes = [int(i) for i in file]

boxes = sorted(boxes)
count = []
for box in boxes:
    if box <= s:
        s -= box
        count.append(box)
    else:
        break

s += count.pop()
boxes = sorted(boxes)[::-1]
for box in boxes:
    if box <= s:
        count.append(box)
        break

print(len(count), count[-1])
