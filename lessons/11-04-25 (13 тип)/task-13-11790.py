from ipaddress import *

for mask in range(16, 25):
    net = ip_network(f"152.65.245.132/{mask}", False)
    cnt = 0
    for i in net:
        i = f"{int(i):032b}"
        prav = i[16:]
        lev = i[:16]
        if lev.count("0") >= prav.count("0"):
            cnt += 1
    if cnt == len(list(net)):
        print(mask - 16)
        #в ручную ищем число в 10-ой системе
        break