with open("26_4604 (1).txt") as file:
    n = file.readline()
    boxes = [int(i) for i in file]

boxes = sorted(set(boxes))[::-1]
last = boxes[0]
cnt = 1
for box in boxes:
    if last - box >= 3:
        cnt += 1
        last = box

print(cnt, last)
