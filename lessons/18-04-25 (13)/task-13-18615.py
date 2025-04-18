from ipaddress import *

ip = ip_address("143.131.211.37")
for mask in range(32, 1, -1):
    cnt = 0
    net = ip_network(f"{ip}/{mask}", False)
    for i in net:
        i = f"{int(i):032b}"
        if i.count("1") == 10:
            cnt += 1
        if cnt > 15:
            break
    if cnt == 15:
        print(mask)
