from ipaddress import *

for a in range(256):
    net = ip_network(f"127.63.67.1/255.255.{a}.0", False)
    for i in net:
        i = f"{int(i):032b}"
        if i[:16].count("1") < i[16:].count("1"):
            break
    else:
        print(a)