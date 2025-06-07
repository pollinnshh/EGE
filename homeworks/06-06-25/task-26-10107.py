with open("26_10107.txt") as file:
    n = int(file.readline())
    events = [list(map(int, i.split())) for i in file]

events = sorted(events, key=lambda x: (x[1]))
true = [events[0]]
for event in events:
    if true[-1][1] <= event[0]:
        true.append(event)

print(len(true), true[-1][0] - true[-2][1])
