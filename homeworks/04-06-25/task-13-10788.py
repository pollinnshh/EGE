from ipaddress import *

ip_1 = ip_address("201.44.240.33")
ip_2 = ip_address("201.44.240.107")

cnt = 0
for mask in range(32):
    net_1 = ip_network(f"{ip_1}/{mask}", False)
    net_2 = ip_network(f"{ip_2}/{mask}", False)
    if net_1 == net_2:
        if net_1.network_address != ip_1 and ip_1 != net_1.broadcast_address:
            if net_2.network_address != ip_2 and ip_2 != net_2.broadcast_address:
                if f"{int(net_1.network_address):032b}".count("1") >= 5:
                    cnt += 1
print(cnt)
