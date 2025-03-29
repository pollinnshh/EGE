with open("2600.txt") as file:
    n = file.readline()
    trucks = [list(map(int, i.split())) for i in file]

trucks = sorted(trucks)
for i in range(len(trucks)):
    trucks[i].append(trucks[i][0] + ((trucks[i][1] + (10 - trucks[i][1] % 10)) // 10))

time = 0
ans = []
for i in range(len(trucks) - 1):
    truck1 = trucks[i]
    truck2 = trucks[i + 1]
    if time > truck2[0]:
        time = truck1[2]
    else:
        ans.append(truck2[1])

#https://kompege.ru/variant?kim=25090569
