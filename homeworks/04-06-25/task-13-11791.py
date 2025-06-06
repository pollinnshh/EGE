from ipaddress import *

for a in range(16, 25):
    net = ip_network(f"246.51.128.202/{a}", False)
    for i in net:
        i = f"{int(i):032b}"
        if i[:16].count("0") > i[16:].count("0"):
            break
    else:
        print(net.netmask)
