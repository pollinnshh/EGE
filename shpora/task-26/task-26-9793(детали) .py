with open("26_9793.txt") as file:
    n = int(file.readline())
    details = []
    for pos, i in enumerate(file, 1):
        sh, po = map(int, i.split())
        details.append([sh, 1, pos])   # шлифовка
        details.append([po, 2, pos])   # покраска

details = sorted(details)

conveyor = [0] * n
last = 0
for time, type, num in details:
    if num not in conveyor:
        if type == 1:
            free = conveyor.index(0)
            conveyor[free] = num
        else:
            free = conveyor[::-1].index(0)
            conveyor[n - free - 1] = num
        last = num

print(last, conveyor.index(last))
