with open("26_10107.txt") as file:
    n = int(file.readline())
    events = [list(map(int, i.split())) for i in file]

events = sorted(events, key=lambda x: x[1])

approved = [events[0]]
for event in events:
    if approved[-1][1] <= event[0]:
        approved.append(event)

last = approved.pop()
for event in events:
    if approved[-1][1] <= event[0] and event[0] > last[0]:
        print(event)
print(len(approved) + 1, last[0] - approved[-1][1])  # проверка есть ли выгодней разница между началом и концом
