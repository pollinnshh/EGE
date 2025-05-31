with open("26_4712.txt") as file:
    n = file.readline()
    boxes = [int(i) for i in file]

boxes = sorted(boxes)[::-1]
last_box = boxes[0]
cnt = 1
for box in boxes:
    if last_box - box >= 3:
        cnt += 1
        last_box = box
print(cnt, last_box)
