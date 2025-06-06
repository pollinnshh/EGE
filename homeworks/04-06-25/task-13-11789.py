from ipaddress import *

for a in range(16, 25):
    net = ip_network(f"99.8.254.232/{a}", False)
    for i in net:
        i = f"{int(i):032b}"
        if i[:16].count("1") > i[16:].count("1"):
            break
    else:
        print(net.netmask)
