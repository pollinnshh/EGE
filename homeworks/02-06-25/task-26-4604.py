with open("26_4604.txt") as file:
    n = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes)[::-1]
last = boxes[0]
cnt = 1
for box in boxes:
    if last - box >= 3:
        cnt += 1
        last = box

print(cnt, last)
