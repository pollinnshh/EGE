from ipaddress import *

ip_1 = ip_address("112.117.107.70")
ip_2 = ip_address("112.117.121.80")
for mask in range(30, 0, -1):
    net1 = ip_network(f"{ip_1}/{mask}", False)
    net2 = ip_network(f"{ip_2}/{mask}", False)
    if net1.network_address == net2.network_address:
        if ip_1 != net1.broadcast_address and ip_1 != net1.network_address:
            if ip_2 != net2.broadcast_address and ip_2 != net2.network_address:
                print(2 ** (32 - mask))
                break
