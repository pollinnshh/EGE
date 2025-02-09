with open("26_9711.txt") as file:
    m, n = map(int, file.readline().split())
    scooters = []
    max_time = 0
    for line in file:
        a, b, c, d = map(int, line.split())
        scooters.append([a, a + b + 1, c, d])
        if max_time < a + b + 1:
            max_time = a + b + 1

scooters = sorted(scooters)

start_scooters = [0] * (m + 1)
used_scooters = []
for i in range(m + 1):
    used_scooters.append([])
for scooter in scooters:
    start_time = scooter[0]
    end_time = scooter[1]
    start_parking = scooter[2]
    end_parking = scooter[3]
    if len(used_scooters[start_parking]) != 0 \
            and min(used_scooters[start_parking]) <= start_time:
        used_scooters[start_parking].remove(min(used_scooters[start_parking]))
    else:
        start_scooters[start_parking] += 1

    used_scooters[end_parking].append(end_time)
print(start_scooters.index(max(start_scooters)))

time_line = [0] * max_time
for scooter in scooters:
    start_time = scooter[0]
    end_time = scooter[1]
    for i in range(start_time, end_time):
        time_line[i] += 1

print(time_line.index(max(time_line)))
