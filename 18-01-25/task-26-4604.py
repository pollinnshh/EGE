## 1 способ
with open("26_4604.txt") as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(set(boxes))[::-1]  # sorted(boxes, reverse=True)
last_box = boxes[0]
count = 1
for box in boxes:
    if last_box - box >= 3:
        count += 1
        last_box = box
print(count, last_box)

## 2 способ
with open("26_4604.txt") as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)
true_boxes = [boxes[0]]
for box in boxes:
    if true_boxes[-1] - box >= 3:
        true_boxes.append(box)
print(len(true_boxes), min(true_boxes))