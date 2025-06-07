with open("26_21424.txt") as file:
    n = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes)[::-1]
last = boxes[0]
cnt = 1
for box in boxes:
    if last - box >= 9:
        last = box
        cnt += 1

print(cnt, last)
