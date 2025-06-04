from ipaddress import *

for a in range(256):
    net = ip_network(f"192.214.{a}.184/255.255.255.224", False)
    for i in net:
        i = f"{int(i):032b}"
        if not (i.count("1") > 15):
            break
    else:
        print(a)