from ipaddress import *

ans = []
for a in range(256):
    net = ip_network(f"246.81.65.{a}/255.255.255.224", False)
    if ip_address(f"246.81.65.{a}") != net.network_address and ip_address(f"246.81.65.{a}") != net.broadcast_address:
        for i in net:
            i = f"{int(i):032b}"
            if i[16:24].count("0") < i[24:].count("0"):
                break
        else:
            ans.append(a)
print(len(set(ans)))