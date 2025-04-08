with open("") as file:
    n = file.readline()
    boxes = [int(i) for i in file]

boxes = sorted(boxes)[::-1]
