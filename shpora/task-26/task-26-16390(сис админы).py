with open("26_16390.txt") as file:
    s, n = map(int, file.readline().split())
    boxes = [int(i) for i in file]

boxes = sorted(boxes)
cnt = []
for box in boxes:
    if box <= s:
        s -= box
        cnt.append(box)
    else:
        break

s += cnt.pop()
boxes = sorted(boxes)[::-1]
for box in boxes:
    if box <= s:
        cnt.append(box)
        break
print(len(cnt), cnt[-1])